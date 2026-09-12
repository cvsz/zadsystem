from decimal import Decimal

import pytest

from src.service_broker import AcquisitionEvent


def _event(**overrides):
    values = {
        "tenant_id": "tenant-zeaz",
        "service_id": "automation",
        "channel": "google-ads",
        "campaign_id": "cmp-002",
        "lead_id": "lead-002",
        "landing_page": "https://www.zeaz.dev/services/automation",
        "expected_revenue": Decimal("20000"),
        "expected_supplier_cost": Decimal("8000"),
        "expected_variable_ops": Decimal("1000"),
        "expected_risk_reserve": Decimal("1000"),
        "expected_cac": Decimal("2000"),
    }
    values.update(overrides)
    return AcquisitionEvent(**values)


def test_service_broker_economics_example():
    event = _event(
        service_id="landing-page",
        campaign_id="cmp-001",
        lead_id="lead-001",
        landing_page="https://www.zeaz.dev/services/landing-page",
        expected_revenue=Decimal("15000"),
        expected_supplier_cost=Decimal("9000"),
        expected_variable_ops=Decimal("1000"),
        expected_risk_reserve=Decimal("500"),
        expected_cac=Decimal("1500"),
    )

    assert event.contribution() == Decimal("3000")
    assert event.contribution_margin() == Decimal("0.2")
    assert not event.passes_guardrails()


def test_guardrails_accept_healthy_campaign_and_preserve_tenant_scope():
    event = _event()

    assert event.contribution() == Decimal("8000")
    assert event.contribution_margin() == Decimal("0.4")
    assert event.passes_guardrails()
    contract = event.to_contract()
    assert contract["schema_version"] == "service-broker.acquisition.v1"
    assert contract["tenant_id"] == "tenant-zeaz"
    assert contract["expected_contribution"] == "8000"


@pytest.mark.parametrize(
    "field_name",
    ["tenant_id", "service_id", "channel", "campaign_id", "lead_id"],
)
def test_routing_identity_fails_closed_when_missing(field_name):
    with pytest.raises(ValueError, match=field_name):
        _event(**{field_name: "   "})
