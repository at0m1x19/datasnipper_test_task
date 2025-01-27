from playwright.sync_api import Page, expect

from src.pages.base_page import BasePage


class RoiCalculatorPage(BasePage):
    ROI_RESOURCE = "/roi-calculator-external-audit"

    def __init__(self, page: Page, base_host: str):
        super().__init__(page, base_host)

        self._calculator_iframe = page.frame_locator("iframe[title='External Audit - DataSnipper ROI Report']")

        self.start_btn = self._calculator_iframe.locator("#landingBtn")
        self.first_step_question = self._calculator_iframe.locator(
            "text=What's your yearly number of audit engagements?")
        self.first_step_progressbar = self._calculator_iframe.locator(".progress.newProgressbar")
        self.first_step_input = self._calculator_iframe.locator('input[type="text"][placeholder="e.g. 500"]')
        self.first_step_next_btn = self._calculator_iframe.get_by_role("link", name="keyboard_arrow_right")

    def open(self):
        self.page.goto(f"{self.base_host}{self.ROI_RESOURCE}")
        expect(self.start_btn).to_be_enabled()
        return self

    def validate_start_calculating_button(self):
        expect(self.start_btn).to_be_visible()
        return self

    def click_start_calculating(self):
        self.start_btn.click()
        return self

    def validate_first_step(self):
        expect(self.first_step_question).to_be_visible()
        expect(self.first_step_progressbar).to_be_visible()
        expect(self.first_step_input).to_be_visible()
        expect(self.first_step_next_btn).to_be_enabled()
        return self
