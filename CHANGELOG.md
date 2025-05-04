# Changelog

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
