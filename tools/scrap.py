from typing import Any, Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.base import WaterCrawlBaseMixin


class ScrapTool(WaterCrawlBaseMixin, Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        format = tool_parameters.get('format') or "markdown"
        include_links = tool_parameters.get("include_links", False)
        timeout = tool_parameters.get("timeout", 15000)
        wait_time = tool_parameters.get("wait_time", 1000)
        actions = []

        if format == 'screenshot':
            actions.append({
                'type': 'screenshot',
            })

        response = self.client.scrape_url(
            url=tool_parameters["url"],
            download=True,
            page_options={
                'include_html': format == 'html',
                'include_links': include_links,
                'timeout': timeout,
                'wait_time': wait_time,
                'actions': actions
            }
        )

        if not response:
            yield self.create_text_message(
                'No result found for the given URL'
            )
            return

        self.create_json_message(
            response
        )

        result = response.pop('result')
        markdown = result.get('markdown')
        html = result.get('html')

        if format == 'markdown' and markdown:
            yield self.create_text_message(markdown)
            if include_links:
               self.create_text_message("\n".join(result['links']))
            return
        elif format == 'html' and html:
            yield self.create_text_message(html)
            return
        elif format == 'screenshot':
            for attachment in response['attachments']:
                yield self.create_link_message(attachment['attachment'])
            return
        else:
            yield self.create_json_message(
                result
            )
            return