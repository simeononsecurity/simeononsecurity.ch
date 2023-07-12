# SimeonOnSecurity Website Source

The source code for the [SimeonOnSecurity](https://SimeonOnSecurity.ch) website 

### Badges:
[![Netlify Status](https://api.netlify.com/api/v1/badges/190394fe-722e-4aa2-bc39-ff81985b2960/deploy-status)](https://app.netlify.com/sites/simeononsecurity/deploys)
![Hugo Build](https://github.com/simeononsecurity/simeononsecurityweb/workflows/hugo/badge.svg)
![Greetings](https://github.com/simeononsecurity/simeononsecurityweb/workflows/Greetings/badge.svg)
![Mark stale issues and pull requests](https://github.com/simeononsecurity/simeononsecurityweb/workflows/Mark%20stale%20issues%20and%20pull%20requests/badge.svg)
[![VirusTotal Scan](https://github.com/simeononsecurity/simeononsecurity.ch/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/simeononsecurity.ch/actions/workflows/virustotal.yml)

### Technologies used:
- [CloudFlare](https://www.cloudflare.com/)
    - Used for Proxy, CDN, Caching, Country Blocking
    - [CloudFlare Wrangler Action](https://github.com/cloudflare/wrangler-action)
      - Used for Automating Deploying Cloudflare Workers
      - [CloudFlare AMP Optimizer](https://github.com/ampproject/cloudflare-amp-optimizer)
        - SEO and Mobile Friendly Site Optimizer
      - [CloudFlare Workers Site Template](https://github.com/xJonathanLEI/cf-workers-site-template)
        - Used to Cache Website with Increased Locality
- [Hugo Extended](https://gohugo.io/)
    - Used for Static Site Generation
- [Hugo - Hello Friend Theme](https://themes.gohugo.io/hugo-theme-hello-friend/)
    - Self Explanatory
    - [node.js](https://nodejs.org/en/)
        - Dependency of Hello Friend
        - Used for dynamic theme generation.
- [Netlify](https://www.netlify.com/)
    - Used for Hosting, SSL Registration, Forms, Automated Hugo Site Generation
- [glotta](https://github.com/simeononsecurity/glotta)
  - Used for article translations. Supports 16 languages. Developed by [1nf053c](https://github.com/1nf053c).
- [Progressive Web App / Service Workers](https://web.dev/progressive-web-apps/)
    - Used to increase usability and accessability of the site.
    - Looking for help with https://github.com/simeononsecurity/simeononsecurity.ch/issues/487

### Responsible Disclosure:
SimeonOnSecurity.ch supports the [security.txt](https://securitytxt.org/) [RFC](https://tools.ietf.org/html/draft-foudil-securitytxt-10). 

Find relevant details for reporting any security concerns or vulnrabilities with our website or any of our repos [here](https://simeononsecurity.ch/.well-known/security.txt)
- Verified reports will be posted in the [SimeonOnSecurity Hall of Fame](https://simeononsecurity.ch/hof)
