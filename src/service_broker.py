"""Service-broker acquisition adapter.

Keeps zadsystem focused on acquisition while emitting a stable event contract that
zworkforce can consume. The module deliberately contains no marketplace-specific
logic and defaults to dry-run economics so ad spend cannot be activated by this
adapter itself.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from decimal import Decimal
from typing import Any


@dataclass(frozen=True)
class AcquisitionEvent:
    tenant_id: str
    service_id: str
    channel: str
    campaign_id: str
    lead_id: str
    landing_page: str
    expected_revenue: Decimal
    expected_supplier_cost: Decimal
    expected_variable_ops: Decimal
    expected_risk_reserve: Decimal
    expected_cac: Decimal
    currency: str = "THB"
    schema_version: str = "service-broker.acquisition.v1"

    def __post_init__(self) -> None:
        """Fail closed when routing identity is missing.

        Tenant scope is part of the service-broker security boundary. Acquisition
        events without an explicit tenant must never be forwarded into shared
        orchestration where they could be attributed to the wrong customer.
        """

        required_identity = {
            "tenant_id": self.tenant_id,
            "service_id": self.service_id,
            "channel": self.channel,
            "campaign_id": self.campaign_id,
            "lead_id": self.lead_id,
        }
        for field_name, value in required_identity.items():
            if not value or not value.strip():
                raise ValueError(f"{field_name} must be a non-empty string")

    def contribution(self) -> Decimal:
        return self.expected_revenue - (
            self.expected_supplier_cost
            + self.expected_variable_ops
            + self.expected_risk_reserve
            + self.expected_cac
        )

    def contribution_margin(self) -> Decimal:
        if self.expected_revenue <= 0:
            return Decimal("0")
        return self.contribution() / self.expected_revenue

    def passes_guardrails(
        self,
        *,
        minimum_contribution: Decimal = Decimal("3000"),
        minimum_margin: Decimal = Decimal("0.30"),
        maximum_cac_ratio: Decimal = Decimal("0.15"),
    ) -> bool:
        if self.expected_revenue <= 0:
            return False
        return (
            self.contribution() >= minimum_contribution
            and self.contribution_margin() >= minimum_margin
            and self.expected_cac / self.expected_revenue <= maximum_cac_ratio
        )

    def to_contract(self) -> dict[str, Any]:
        payload = asdict(self)
        for key, value in list(payload.items()):
            if isinstance(value, Decimal):
                payload[key] = str(value)
        payload["expected_contribution"] = str(self.contribution())
        payload["expected_contribution_margin"] = str(self.contribution_margin())
        return payload
