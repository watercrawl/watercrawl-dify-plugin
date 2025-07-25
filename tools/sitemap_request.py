from typing import Any, Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from requests import HTTPError

from tools.base import WaterCrawlBaseMixin


class SitemapTool(WaterCrawlBaseMixin, Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        options = {
            "include_subdomains": tool_parameters.get("include_subdomains", True),
            "ignore_sitemap_xml": tool_parameters.get("ignore_sitemap_xml", False),
            "search": tool_parameters.get("search", None),
            "include_paths": [],
            "exclude_paths": []
        }

        try:
            sitemap_request = self.client.create_sitemap_request(
                url=tool_parameters["url"],
                options=options,
            )
        except HTTPError as e:
            if 400 <= e.response.status_code < 500:
                yield self.create_json_message({
                    'status_code': e.response.status_code,
                    'response': e.response.json()
                })
                return
            raise e

        for result in self.client.monitor_sitemap_request(sitemap_request['uuid'], download=True):
            if result['type'] == 'state' and result['data']['status'] == 'finished':
                sitemap_request = result['data']
                yield self.create_json_message(sitemap_request)
                yield self.create_text_message(self.client.get_sitemap_results(sitemap_request, 'markdown'))
                break
