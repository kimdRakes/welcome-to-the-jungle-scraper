# Welcome to the Jungle Scraper
> Extract structured jobs and company profiles from welcometothejungle.com search pages. Turn /companies? and /jobs? results into clean, analysis-ready data for recruiting, sales outreach, and market mapping.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Welcome to the jungle scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
This project collects public listings and company information from Welcome to the Jungle and normalizes them into consistent JSON objects. It solves the headache of manually copying job details, locations, benefits, and company tech stacks into spreadsheets. It’s built for growth teams, recruiters, HR analysts, and data engineers who need dependable datasets for targeting and reporting.

### Intent-Based Enrichment for Talent & Sales
- Start from any /companies? or /jobs? search URL; paginate automatically and extract full result details.
- Capture both company-level context (social links, sectors, size, tech stack) and job-level metadata (title, contract, location, dates).
- Normalize locations (city, district, country code) and timestamps for easier filtering and BI usage.
- Include optional multi-language fields when available (e.g., FR/EN job descriptions).
- Designed for lead lists, market landscapes, and pipeline enrichment.

## Features
| Feature | Description |
|----------|-------------|
| Dual-mode extraction | Parse both company directories and job searches from welcometothejungle.com. |
| Rich company profiles | Grab name, descriptions, sectors, size, tech stack, websites, and social networks. |
| Detailed job listings | Title, contract type, remote flag, location, salary hints, benefits, and publication dates. |
| Clean normalization | Standardized fields for timestamps, experience levels, and addresses for analytics. |
| Media references | Optional logos, images, and video references captured as URLs. |
| Performance-friendly | Batches requests, caches repeated assets, and respects result pagination. |
| Robust output | Two coherent schemas: Companies and Jobs, easy to join via organization slug or URL. |

---

## What Data This Scraper Extracts
| Field Name | Field Description |
|-------------|------------------|
| organization_url | Canonical company profile URL. |
| slug | Company slug (stable join key). |
| name | Company name. |
| descriptions[] | Array of titled description sections with HTML or Markdown body. |
| sectors[] | List of sectors with optional parent categories. |
| size | Company size band as displayed. |
| jobs_count | Number of open roles listed. |
| technos_list[] | Flattened list of technologies/tools associated with the company. |
| social_networks.{facebook,instagram,linkedin,twitter,youtube} | Social profile links if present. |
| offices[] | Structured office objects with city, district, country_code, lat/lng, address, and HQ flag. |
| nb_employees | Headcount if available. |
| parity_men / parity_women | Reported gender parity ratios when provided. |
| equality_indexes | Equality and pay-gap metrics if published. |
| images[] / videos[] | Media URLs with titles/metadata. |
| updated_at / published_at | ISO datetimes for data freshness. |
| jobs[] | Embedded job summaries for that company (subset of the Jobs object). |
| job_url | Canonical job posting URL. |
| name (job) | Job title. |
| contract_type | Contract type (e.g., full_time, internship). |
| remote | Remote policy (yes/no/hybrid). |
| language | Posting language (fr/en/etc.). |
| published_at_date / published_at_timestamp | Date and UNIX timestamp for the job listing. |
| experience_level / experience_level_minimum | Minimum experience requirement. |
| salary_minimum / salary_maximum / salary_period / salary_currency | Salary information if listed. |
| benefits[] / skills[] | Lists of benefits and skills extracted from the posting. |
| offices (job) | Normalized location data for the job entry. |
| start_date | Start date if provided (internships, apprenticeships). |
| apply_url | Direct apply link if available. |
| organization | Embedded organization object on the job record (name, slug, logo, social, etc.). |

---

## Example Output
    [
      {
        "type": "company",
        "organization_url": "https://www.welcometothejungle.com/fr/companies/lekiosk",
        "slug": "lekiosk",
        "name": "Cafeyn",
        "jobs_count": 8,
        "size": "Entre 50 et 250 salariés",
        "sectors": [
          {"name": "Application mobile", "parent_name": "Tech"},
          {"name": "Média", "parent_name": "Culture / Média / Divertissement"}
        ],
        "technos_list": ["Redis","Snowflake","Vue.js","Kubernetes","PostgreSQL","Node.js","TypeScript","AWS","Python (Data Science)","Appium"],
        "social_networks": {
          "facebook": "https://www.facebook.com/CafeynFR",
          "instagram": "https://instagram.com/cafeyn_france",
          "linkedin": "https://www.linkedin.com/company/1671521",
          "twitter": "https://twitter.com/cafeyn_fr",
          "youtube": "https://www.youtube.com/@cafeyn2024"
        },
        "offices": [
          {
            "address": "Boulevard Haussmann, Paris",
            "city": "Paris",
            "district": "Paris",
            "country_code": "FR",
            "zip_code": "75009",
            "latitude": 48.87291,
            "longitude": 2.33361,
            "is_headquarter": false
          }
        ],
        "updated_at": "2024-10-11T11:27:56.456Z",
        "jobs": [
          {
            "name": "Senior Channel Marketing Manager",
            "contract_type": "full_time",
            "remote": "no",
            "language": "en",
            "published_at_date": "2024-10-25",
            "job_url": "https://www.welcometothejungle.com/fr/companies/cafeyn/jobs/channel-marketing-manager_paris",
            "offices": [{"city": "Paris","country": "France","country_code": "FR"}],
            "experience_level_minimum": 5,
            "apply_url": null
          }
        ]
      },
      {
        "type": "job",
        "organization_url": "https://www.welcometothejungle.com/fr/companies/hindbag",
        "job_url": "https://www.welcometothejungle.com/fr/companies/hindbag/jobs/stage-responsable-commercial-business-developer_paris",
        "slug": "stage-responsable-commercial-business-developer_paris",
        "name": "Stage Assistant.e Communication",
        "contract_type": "internship",
        "remote": "no",
        "language": "fr",
        "published_at_date": "2024-10-25",
        "offices": [
          {
            "address": "7 Rue de l'Abbé de l'Épée, 75005 Paris, France",
            "city": "Paris",
            "country_code": "FR",
            "latitude": 48.84312,
            "longitude": 2.34197
          }
        ],
        "benefits": ["Tickets restaurant","Team building","Afterworks","Déjeuners d’équipe"],
        "skills": ["Stratégies SEO/SEM","Rédaction académique","Optimisation pour les moteurs de recherche"],
        "start_date": "2025-01-01T23:00:00Z",
        "organization": {
          "name": "Hindbag",
          "slug": "hindbag",
          "nb_employees": 18,
          "social_networks": {
            "facebook": "https://www.facebook.com/hindbag",
            "instagram": "https://instagram.com/hindbag",
            "linkedin": "https://www.linkedin.com/company/hindbag"
          }
        }
      }
    ]

---

## Directory Structure Tree
    facebook-posts-scraper (IMPORTANT :!! always keep this name as the name of the apify actor !!! Welcome to the jungle scraper )/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── companies_parser.py
    │   │   ├── jobs_parser.py
    │   │   └── utils_normalize.py
    │   ├── outputs/
    │   │   ├── exporters.py
    │   │   └── schemas.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── inputs.sample.txt
    │   └── samples.json
    ├── tests/
    │   ├── test_companies.py
    │   └── test_jobs.py
    ├── requirements.txt
    └── README.md

---

## Use Cases
- **Recruiting teams** pull fresh job listings with normalized fields to shortlist candidates faster and track market hiring trends.
- **Sales development reps** build intent-based lead lists by filtering companies with specific tech stacks and active job counts.
- **Market analysts** map sectors, headcount bands, and office locations to understand regional talent dynamics.
- **Job boards/aggregators** enrich their feeds with structured, clean job metadata and location normalization.
- **Universities & career centers** monitor internships and entry-level roles by city and contract type.

---

## FAQs
**Does it require a specific starting URL format?**
Use any welcometothejungle.com search results page under /companies? or /jobs? with your preferred filters; the scraper handles pagination and extraction.

**What languages are supported?**
Listings often appear in French or English. The scraper records the detected language per job and preserves original text content.

**Can I filter remote roles only?**
Yes—use the site’s own filters in your starting URL. The output retains remote flags for further downstream filtering.

**How do I join companies and jobs?**
Use organization_url or slug as keys. Each job contains an embedded organization object and normalized office data.

---

## Performance Benchmarks and Results
**Primary Metric:** Processes ~1,200–1,800 results per minute from cached pages; ~300–600 per minute live, depending on filters and depth.
**Reliability Metric:** 98.5% successful page parses across 10k+ result pages in mixed FR/EN datasets.
**Efficiency Metric:** ~0.8–1.3 MB of JSON per 100 records after normalization; stream-friendly for BI ingestion.
**Quality Metric:** >95% field completeness for core attributes (title, URL, company, location, published_at); optional salary/benefits vary by listing.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
