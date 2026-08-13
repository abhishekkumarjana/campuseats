# Network Analysis

## Website

Website: https://rpf.indianrailways.gov.in/RPF/

## Test Conditions

- Browser: Google Chrome
- DevTools panel: Network
- Cache: Disabled
- Page was reloaded with DevTools open

## Results

- Total requests: 82
- Total transferred: 13.1 MB
- Total resources: 14.3 MB
- Slowest resource: 22.73 s
- Slowest resource duration: 0 ms

## 400 Responses

Observation: The Network tab shows multiple 404 (Not Found) errors for CSS and JavaScript resources such as chartist.min.js, bootstrap.min.css, custom_scroll.css, popper.min.js, bootstrap.min.js, jquery-ui.min.js, main.css, and main.js. This indicates that these files could not be found at the requested URLs, so some webpage styles or functionality may not load correctly.

## Waterfall Analysis

The Network waterfall shows when the browser requested each resource and how long each request took. The slowest resource was Gallery3.jpg, which took approximately 22.73 ms.

## Observations

The browser requested the resources needed to load the webpage. Disabling the cache allowed the resources to be requested again during the reload.