from playwright.sync_api import Page, expect

from src.pages.base_page import BasePage


class PricingPage(BasePage):
    def __init__(self, page: Page, base_host: str):
        super().__init__(page, base_host)

        self.basic_container = page.locator(
            "div.price-card-v-two:has(h1.heading-5-card-pricing:text('Basic'))"
        )
        self.basic_subtitle = self.basic_container.locator(
            'div.text-block-55:has-text("For small business")'
        )
        self.basic_demo_link = self.basic_container.locator(
            'a[href="/book-demo-basic"]'
        )

        self.professional_container = page.locator(
            "div.price-card-v-two:has(h1.heading-5-card-pricing:text('Professional'))"
        )
        self.professional_subtitle = self.professional_container.locator(
            'div.text-block-55:has-text("For medium-sized business")'
        )
        self.professional_demo_link = self.professional_container.locator(
            'a[href="/book-demo-professional"]'
        )

        self.enterprise_container = page.locator(
            "div.price-card-v-two:has(h1.heading-5-card-pricing:text('Enterprise'))"
        )
        self.enterprise_subtitle = self.enterprise_container.locator(
            'div.text-block-55:has-text("For large enterprise")'
        )
        self.enterprise_demo_link = self.enterprise_container.locator(
            'a[href="/book-demo-enterprise"]'
        )

        self.custom_ocr_row_overview = (page.locator("div.comparison-row-low:has-text('Custom OCR Configuration')")
                                        .locator("div.flex-pricing-checks-overview"))

    def open(self):
        self.page.goto(f"{self.base_host}/pricing")
        expect(self.basic_container).to_be_visible()
        return self

    def validate_basic_plan(self):
        expect(self.basic_subtitle).to_be_visible()
        expect(self.basic_demo_link).to_have_attribute("href", "/book-demo-basic")
        return self

    def validate_professional_plan(self):
        expect(self.professional_subtitle).to_be_visible()
        expect(self.professional_demo_link).to_have_attribute("href", "/book-demo-professional")
        return self

    def validate_enterprise_plan(self):
        expect(self.enterprise_subtitle).to_be_visible()
        expect(self.enterprise_demo_link).to_have_attribute("href", "/book-demo-enterprise")
        return self

    def validate_comparison_table_enterprise_custom_ocr(self):
        expect(self.custom_ocr_row_overview.locator(":scope > *").nth(0)).to_have_class("text-row stripe")
        expect(self.custom_ocr_row_overview.locator(":scope > *").nth(1)).to_have_class("text-row stripe")
        expect(self.custom_ocr_row_overview.locator(":scope > *").nth(2)).to_have_class("image-45")

        return self
