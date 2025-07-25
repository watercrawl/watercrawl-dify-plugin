# Changelog

## [v0.5.0] - 2025-07-25
### Added
- **New Sitemap Tool**: Introduced a new `sitemap` tool to generate a sitemap directly from a URL, with options to include subdomains, ignore `sitemap.xml`, and filter by search terms.
- **Get Single Crawl Result**: The `crawl_job` tool now supports a `get_result` operation to fetch a single crawl result by its UUID.

### Changed
- **Plugin Version**: Updated plugin version to `0.5.0` and declared compatibility with WaterCrawl `v0.9.*`.
- **Deprecated Sitemap Tool**: The previous `sitemap` tool, which operated on completed crawl requests, has been deprecated in favor of the new, more direct sitemap generation tool.
- **Enhanced Tool Feedback**:
    - `crawl`: Now provides richer, real-time feedback, including the crawl request object, a running summary, and final results.
    - `crawl_job`: The `get` operation now returns a concise text summary of the job status.
    - `scrape`: Now outputs the full JSON response, the extracted markdown, and optional HTML for better usability.
    - `search`: Now returns a clear text summary of the search parameters and results.
    - `search_job`: The `get` operation now includes a text summary of the job status and any available results.
- **Simplified Search Job**: The `search_job` tool's `monitor` option has been removed for a cleaner interface; the `get` operation now provides all necessary information.


## [v0.4.0] - 2025-05-04
### Added
- **Search Tool**: Search the web for information using WaterCrawl's search API with configurable options for language, country, time range, and search depth.
- **Search Job Tool**: Retrieve search results or manage search jobs based on a search request UUID. Monitor progress or cancel search tasks as needed.
- **Sitemap Tool**: Retrieve a sitemap from a completed crawl request in various formats (default JSON, graph for visualization, or markdown).

### Changed
- Updated Dify plugin dependency from v0.0.1b60 to v0.2.1
- Improved Scrape Tool with more structured output options:
  - Updated to output markdown by default
  - Added ability to separately toggle HTML inclusion
  - Added screenshot generation option
  - Improved variable output handling
- Authentication URL updated to point to GitHub README instead of the main website

## [v0.3.1] - 2025-02-25
### Added
- Initial release of the WaterCrawl plugin.
- **Crawl Job Tool**: Retrieve scraping results based on a crawl request UUID and cancel ongoing scraping tasks.
- **Crawl Tool**: Initiates a web crawl to extract data from specified URLs with configurable options for including/excluding URL patterns and generating alt text for images.
- **Scrape Tool**: Scrapes a single URL and outputs the content in various formats (markdown, HTML, JSON, or screenshot).
- Comprehensive user guide and privacy policy included.
