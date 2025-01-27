from src.pages.pricing_page import PricingPage
from src.pages.roi_calculator_page import RoiCalculatorPage


def test_pricing_plans(page, base_host):
    """
    Validate Basic/Professional/Enterprise plans,
    only Enterprise has custom OCR in comparison table.
    """
    (
        PricingPage(page, base_host)
        .open()
        .validate_basic_plan()
        .validate_professional_plan()
        .validate_enterprise_plan()
        .validate_comparison_table_enterprise_custom_ocr()
    )


def test_roi_calculator_first_step(page, base_host):
    """
    Validate the ROI calculator's first step after "Start Calculating"
    """
    (
        RoiCalculatorPage(page, base_host)
        .open()
        .validate_start_calculating_button()
        .click_start_calculating()
        .validate_first_step()
    )
