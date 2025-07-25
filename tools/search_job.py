from typing import Any, Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from requests import HTTPError

from tools.base import WaterCrawlBaseMixin


class SearchJobTool(WaterCrawlBaseMixin, Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        operation = tool_parameters.get("operation", "get")
        try:
            search_request = self.client.get_search_request(
                tool_parameters["search_request_uuid"],
                download=True
            )
        except HTTPError as e:
            if e.response.status_code == 404:
                yield self.create_text_message("Search request not found")
                return
            raise e

        if operation in ["get", "monitor"]:
            yield self.create_json_message(search_request)
            text_summary = f"Search uuid: {search_request['uuid']}"
            text_summary += f"\nStatus: {search_request['status']}"
            if search_request['result']:
                text_summary += f"\nNumber of results: {len(search_request['result'])}"
                for result in search_request['result']:
                    text_summary += f"\nTitle: {result['title']}"
                    text_summary += f"\nURL: {result['url']}"
                    text_summary += f"\nDescription: {result['description']}"
            yield self.create_text_message(text_summary)
            return

        if operation == "cancel":
            yield from self.cancel_search_request(search_request)
            return


        raise ValueError(f"Invalid operation: {operation}")

    def cancel_search_request(self, search_request: dict[str, Any]):
        try:
            self.client.stop_search_request(search_request["uuid"])
            yield self.create_text_message("Search request has been canceled")
        except HTTPError as e:
            if e.response.status_code == 404:
                yield self.create_text_message("Search request not found")
                return
            if e.response.status_code == 403:
                yield self.create_text_message("Search request cannot be canceled")
                return
            raise e
