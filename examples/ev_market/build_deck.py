#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A full ~55-page McKinsey-style desk-research deck on the global EV market.

This is a complete, formal client-grade deliverable - not a toy demo - meant to
show the full capability of the toolkit (front matter -> 5 sections with dividers
& mini-TOCs -> closing -> methodology -> appendix), at consulting-report density:
every content page carries an action-title conclusion, a native visual, and a
dense, substantive analysis column.

All figures are ROUND / ILLUSTRATIVE for a public demo - they approximate the
shape of public data but are not exact citations. Replace with your own verified,
traceable numbers. No client-confidential content.

    python examples/ev_market/build_deck.py   ->  output/ev_market.pptx
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))

from deckforge import Deck, charts, tables, frameworks  # noqa: E402

OUT = os.path.join(HERE, "output")
os.makedirs(OUT, exist_ok=True)
IMG = os.path.join(HERE, "..", "..", "assets", "images")


def img(name):
    return os.path.join(IMG, name)

IEA = ("IEA Global EV Outlook (illustrative)", "https://www.iea.org")
BNEF = ("BloombergNEF-style tracker (illus.)", "https://about.bnef.com")
IRENA = ("IRENA energy data (illustrative)", "https://www.irena.org")
OICA = ("OICA production stats (illustrative)", "https://www.oica.net")
FILE = ("Public OEM filings (illustrative)", "https://www.sec.gov")
TRK = ("Industry trackers (illustrative)", "https://www.iea.org")
ICCT = ("ICCT-style analysis (illustrative)", "https://theicct.org")


def K(n):
    return f"Global EV Market  |  Part {n}  |  2026"


def build():
    import glob
    d = Deck(brand="Acme Research", footer="Acme Research")
    d.set_image_pool(sorted(glob.glob(os.path.join(IMG, "pool", "*.jpg"))))

    # ============================ FRONT MATTER ============================
    d.cover("Global EV Market",
            subtitle="Desk research - market, demand, competition, technology & opportunity",
            meta="Sample report - illustrative data - April 2026",
            image_path=img("cover_ev.jpg"))

    d.prose("Disclaimer", [
        "This report is prepared to illustrate the capability of an automated "
        "desk-research workflow. It uses public, illustrative figures only and "
        "contains no client-confidential information. Numbers approximate the shape "
        "of publicly reported data but are rounded and should not be quoted as exact.",
        "Before any decision, validate every figure against primary, licensed "
        "sources (for example the IEA Global EV Outlook, BloombergNEF, ICCT and "
        "audited OEM filings). Forward-looking years are marked 'E' for estimate and "
        "reflect a desk-research view, not a forecast model.",
    ])

    d.core_questions(
        "Three questions this report sets out to answer",
        "Structured throughout as: question -> evidence -> implication for a challenger.",
        [(1, "Is growth still there?", "Market & momentum",
          ["How fast are EV sales still growing, and for how long does the "
           "S-curve keep its slope?",
           "Where is the ~18% sales share heading by 2030 across regions?",
           "Which regions and price bands carry the next leg of growth?"]),
         (2, "Who is winning, and how?", "Competition",
          ["Which business models out-earn - vertical integration or cost "
           "leadership - and why?",
           "How fast are Chinese OEMs taking global share and resetting cost?",
           "Where does durable margin actually sit in the value chain?"]),
         (3, "Where is the opportunity?", "Strategy",
          ["Which segments and layers are still open to a new entrant?",
           "Is the profit pool migrating from hardware to software and services?",
           "What three or four moves should a challenger prioritise, and when?"])],
    )

    d.agenda("Contents", [
        (1, "Market & momentum - size, growth, regions, drivers and policy"),
        (2, "Demand & buyers - segments, BEV/PHEV mix, total cost and barriers"),
        (3, "Competitive landscape - share, archetypes, China and the supply chain"),
        (4, "Technology & trends - batteries, charging, software and autonomy"),
        (5, "Opportunities & strategy - where the next decade is won"),
    ])

    d.prose("Executive summary - five things that matter", [
        ("Growth is real but decelerating.", "Sales roughly tripled between 2020 and "
         "2025 to about 17m units, equal to roughly 18% of all new cars. But the "
         "year-on-year growth rate is cooling from over 50% to the low-20s as the "
         "early-adopter base saturates and subsidies are withdrawn. This is a "
         "maturing market entering its mainstream phase, not a stalling one."),
        ("The market is concentrated and uneven.", "China, Europe and North America "
         "take the large majority of volume, but each runs on a different driver - "
         "cost parity, emissions mandates and tax credits respectively - and on very "
         "different charging and pricing trajectories. There is no single global "
         "playbook; entry must be sequenced market by market."),
        ("Two business models lead, and you must pick one.", "Vertically-integrated "
         "premium players capture margin through brand and software; cost leaders win "
         "on captive battery supply and price. Both work. Firms that straddle both "
         "lanes tend to be sub-scale on each - focus, not breadth, drives returns."),
        ("China has reset the cost frontier.", "Chinese OEMs combine battery control, "
         "fast product cycles and aggressive price ladders, exporting both cars and "
         "the cost benchmark every other player is now measured against. Assume the "
         "frontier is set in China and plan differentiation and local content "
         "accordingly."),
        ("The profit pool is shifting to software and supply.", "As battery prices "
         "fall and powertrains commoditise, durable margin migrates to recurring "
         "software, services, charging and the upstream battery value chain. A "
         "challenger should invest where future margin sits, not only in the metal."),
    ], columns=2)

    # ===================== PART 1 - MARKET & MOMENTUM =====================
    d.section_divider(1, "Market & momentum",
                      "Size, growth, regional landscape, drivers and policy",
                      ["Sales keep climbing as affordable models arrive",
                       "EV share of new-car sales is nearing a tipping point",
                       "Demand stays concentrated in three blocs",
                       "Four structural drivers keep compounding while subsidy fades - so build the case on cost, product and policy, and treat incentives as upside",
                       "Battery cost decline is the master variable",
                       "Charging build-out is racing to keep up",
                       "Policy is tightening from carrots to mandates"],
                      takeaway="Growth is structural, but the next leg depends on "
                               "affordability, charging and the shift from subsidy to mandate.",
                      image_path=img("div_market.jpg"))

    s, r = d.content("Demand keeps climbing as cheaper models arrive, but growth is cooling - so the prize shifts from being early to being cost-competitive at volume",
        body=[("Momentum is intact.", "Global electric-car sales rose from roughly "
               "10m in 2022 to about 17m in 2025E, more than doubling in three years "
               "as a wave of cheaper models pulled demand well beyond the early "
               "adopters who defined the first phase of the market."),
              ("But the pace is cooling.", "Year-on-year growth has eased from over "
               "50% at the start of the decade to the low-20s today. That is the "
               "natural signature of an S-curve maturing - a larger base growing at a "
               "slower percentage, not a market running out of road."),
              ("Affordability is now the swing factor.", "The decisive question is "
               "whether the next price tier can carry volume into genuinely "
               "mass-market segments without eroding already-thin manufacturer "
               "margins. The models that unlock the next cohort sit below today's "
               "average transaction price."),
              "For a challenger, plan for a market that is large, still growing and "
              "increasingly price-sensitive - the prize shifts from being early to "
              "being cost-competitive at volume."],
        kicker=K(1), sources=[IEA, BNEF])
    d.chart_caption(s, r[0], r[1], r[2], "Global electric-car sales", "Units, millions")
    charts.column(s, d.theme, r[0], r[1] + 0.55, r[2], r[3] - 0.6,
                  ["2021", "2022", "2023", "2024", "2025E"],
                  {"Units (m)": [6.6, 10.2, 13.9, 16.0, 17.3]}, highlight=(0, 4))

    s, r = d.content("EV share of new-car sales is nearing a tipping point - past ~5-10% adoption self-reinforces, so plan for a mainstream market, not a niche",
        body=[("Penetration is rising fast.", "EVs reached roughly 18% of new-car "
               "sales in 2025E, up from about 4% in 2020 - the steep middle of the "
               "adoption S-curve, where each year's gain is larger than the last in "
               "absolute terms even as percentage growth cools."),
              ("Tipping points cluster early.", "Evidence across markets suggests "
               "that once EVs pass roughly 5-10% of sales, adoption tends to "
               "self-reinforce: model choice widens, a used-EV supply forms, charging "
               "density improves and social proof builds. Several large markets have "
               "now crossed that threshold."),
              ("The end-state is mainstream, not niche.", "On current trajectory the "
               "market is mainstream well before 2030 in the leading regions. Pricing, "
               "after-sales service, financing and channel must therefore be designed "
               "for scale and for less technical, more value-driven buyers."),
              "A challenger that plans only for today's penetration will be "
              "structurally under-built for the volume arriving over the plan period."],
        kicker=K(1), sources=[IEA, ICCT])
    d.chart_caption(s, r[0], r[1], r[2], "EV share of new-car sales", "%, global")
    charts.line(s, d.theme, r[0], r[1] + 0.55, r[2], r[3] - 0.7,
                ["2020", "2021", "2022", "2023", "2024", "2025E"],
                {"EV share %": [4, 8, 13, 16, 17, 18]})

    s, r = d.content("Sales stay concentrated in three blocs, each on a different driver - so market entry must be sequenced and localised, not copy-pasted",
        body=[("Concentration is high.", "China, Europe and North America together "
               "account for the large majority of global EV sales. China alone is "
               "more than half the market; the rest of the world is small today but "
               "is growing fastest off a low base, often led by two- and "
               "three-wheelers rather than passenger cars."),
              ("Each bloc runs on a different driver.", "China is propelled by cost "
               "parity and an unmatched density of affordable models; Europe by CO2 "
               "mandates and fleet demand; North America by tax credits tied to local "
               "content. The same product can therefore succeed or fail depending on "
               "which lever the local market pulls."),
              ("A copy-paste strategy fails.", "Because the drivers, price points and "
               "charging contexts differ so sharply, a model and go-to-market that "
               "wins in one bloc rarely transfers intact to another. Entry has to be "
               "sequenced and localised."),
              "For a challenger the first battles are won in a handful of markets - "
              "choose them by fit with your model, not by headline size alone."],
        kicker=K(1), sources=[IEA, TRK])
    d.chart_caption(s, r[0], r[1], r[2], "EV sales by region", "Share of global units, 2025E")
    charts.doughnut(s, d.theme, r[0], r[1] + 0.55, r[2] - 0.4, r[3] - 0.7,
                    ["China", "Europe", "N. America", "Rest of world"],
                    [55, 22, 12, 11], highlight_idx=0)

    s, r = d.wide_slide("Each region runs on a different driver, stage and risk - so sequence entry by driver-fit, winning where your model matches the local pull first",
        kicker=K(1), sources=[IEA, ICCT])
    tables.table(s, d.theme, r[0], r[1], r[2], 2.85,
        [["Region", "2025E share", "Growth", "Primary driver", "Key risk"],
         ["China", "~55%", "High", "Cost parity + dense affordable model supply", "Price war, overcapacity"],
         ["Europe", "~22%", "Moderate", "CO2 fleet mandates + company-car demand", "Subsidy roll-back, China imports"],
         ["North America", "~12%", "Moderate", "Tax credits tied to local content", "Policy reversal, slow charging"],
         ["Rest of world", "~11%", "Fastest", "Two-/three-wheelers, urban fleets", "Charging & grid gaps, affordability"]],
        col_widths=[2.1, 1.7, 1.5, 4.0, 3.03])
    tables.takeaway_bar(s, d.theme, r[0], r[1] + 3.0, r[2],
        "Sequence markets by driver-fit, not size alone - win where your model "
        "matches the local driver first, then extend into adjacent blocs.")

    s, r = d.content_blocks("Four structural drivers keep compounding while subsidy fades - so build the case on cost, product and policy, and treat incentives as upside",
        blocks=[("Facts", "Adoption is pushed by four compounding forces: falling "
                 "battery cost, a widening model line-up across every segment, "
                 "tightening emissions policy, and improving charging access. A fifth "
                 "force - purchase subsidy - is now being withdrawn in most markets."),
                ("Insights", "The first four drivers are structural and reinforce one "
                 "another; subsidy was always transitional. The markets that keep "
                 "growing after incentives are removed are the ones proving genuine, "
                 "unsubsidised demand - the signal that matters most."),
                ("Implications", "Build the business case on cost, product and "
                 "policy-mandate, and treat any remaining incentive as upside rather "
                 "than foundation. A plan that needs subsidy to clear hurdle rates is "
                 "a plan exposed to the one driver that is fading.")],
        kicker=K(1), sources=[IEA, ICCT])
    frameworks.kpi_grid(s, d.theme, r[0], r[1], r[2], r[3],
        [("Cost", "Battery decline", "the master variable"),
         ("Choice", "Model line-up", "every segment covered"),
         ("Policy", "Carrots to mandates", "structural, tightening"),
         ("Charging", "Access improving", "density rising fast")], cols=2)

    s, r = d.content("Falling battery cost is the master variable behind price parity - and below parity, competition shifts from powertrain to software and total cost",
        body=[("Costs keep falling.", "Battery pack costs trended down materially "
               "across 2020-2025, driven by scale, chemistry shifts toward LFP and "
               "manufacturing learning. This is the single biggest lever on EV "
               "sticker price and the main reason credible mass-market models now "
               "exist at all."),
              ("Parity is in sight.", "As pack cost approaches the often-cited "
               "~$80/kWh mark, unsubsidised price parity with comparable combustion "
               "cars becomes realistic in a widening set of segments - first in "
               "China, then Europe, with the entry band the last to cross."),
              ("Below parity, the game changes.", "Once the powertrain no longer "
               "carries a price penalty, it stops being a differentiator. Competition "
               "shifts decisively to software, brand, charging experience and total "
               "cost of ownership - the layers where margin can still be defended."),
              "Track pack cost as the leading indicator of which segments open next; "
              "it is the clock that paces the entire industry."],
        kicker=K(1), sources=[BNEF, IRENA])
    d.chart_caption(s, r[0], r[1], r[2], "Battery pack cost (indexed)", "2020 = 100, illustrative")
    charts.line(s, d.theme, r[0], r[1] + 0.55, r[2], r[3] - 0.7,
                ["2020", "2021", "2022", "2023", "2024", "2025E"],
                {"Cost index": [100, 89, 81, 74, 67, 60]})

    s, r = d.content("Charging build-out races to keep pace with the parc, and fast-charge access is now a purchase driver - a structural opportunity where it lags",
        body=[("Public charging is scaling.", "Public charge-point counts are rising "
               "sharply, led by China, which has installed the bulk of the world's "
               "public points. Yet the ratio of EVs per public charger still varies "
               "widely, and headline counts mask large gaps in reliability and "
               "uptime."),
              ("Fast-charging is the real bottleneck.", "It is DC fast-charge "
               "coverage and grid connection capacity - not slow AC points - that "
               "gate long-distance confidence and commercial-fleet utilisation. The "
               "constraint is increasingly the grid interconnect, not the charger."),
              ("Charging is now a purchase driver.", "Access to convenient charging "
               "at home, at work and en route has become one of the top factors in "
               "the buying decision, and a structural opportunity in under-served "
               "markets where the network is still thin."),
              "For a challenger, a credible charging and energy proposition can be "
              "as decisive as the vehicle itself - especially for fleet buyers."],
        kicker=K(1), sources=[IEA, IRENA])
    d.chart_caption(s, r[0], r[1], r[2], "Public charge points", "Millions, by region (2025E)")
    charts.bar(s, d.theme, r[0], r[1] + 0.55, r[2], r[3] - 0.7,
               ["China", "Europe", "N. America", "RoW"], [3.2, 0.9, 0.4, 0.3],
               highlight_idx=0)

    d.prose("Section 1 takeaways - momentum is structural but maturing", [
        ("Growth is real, not a bubble.", "Penetration is on the steep part of the "
         "S-curve and continues even where subsidies are withdrawn - the strongest "
         "evidence of genuine, unsubsidised demand. Plan for a mainstream market by "
         "2030 in the leading regions."),
        ("It is concentrated and uneven.", "Three blocs dominate, each on a different "
         "driver and at a different stage. Sequence market entry by driver-fit and "
         "localise the model rather than copy-pasting a single playbook."),
        ("Affordability and charging decide the next leg.", "Battery cost and "
         "charging access - not subsidy - are the variables to watch. The next cohort "
         "is won on price-at-volume and on a credible charging proposition."),
    ], kicker=K(1), image_path=img("sum_market.jpg"))

    # ===================== PART 2 - DEMAND & BUYERS =====================
    d.section_divider(2, "Demand & buyers",
                      "Who is buying, what they buy, and what holds them back",
                      ["Buyers are broadening from early adopters to mainstream",
                       "BEV is winning the long run; PHEV is a bridge",
                       "Demand is splitting into three price bands with different economics - so pick one deliberately, because the mass middle competes margin away",
                       "Total cost of ownership already favours EVs, but buyers anchor on sticker price - so sell whole-life cost, financing and energy as one package",
                       "Range, charging and price remain the top barriers",
                       "A used-EV market is forming - and it matters"],
                      takeaway="Demand is mainstreaming, but price, charging and "
                               "residual-value confidence still gate the next cohort.",
                      image_path=img("div_demand.jpg"))

    s, r = d.wide_slide("Buyers are broadening to a pragmatic mainstream that buys on total cost, reliability and charging - not novelty, so design the offer for them",
        kicker=K(2), sources=[ICCT, TRK])
    tables.table(s, d.theme, r[0], r[1], r[2], 2.85,
        [["Buyer segment", "Share of EV buyers", "What they want", "How to win them"],
         ["Early adopters", "Shrinking", "Technology, brand, performance", "Hero product, software cadence"],
         ["Pragmatic mainstream", "Growing fast", "Total cost, reliability, charging", "Value, service, trusted residuals"],
         ["Fleet / commercial", "Large & sticky", "Uptime, cost-per-km, support", "Whole-life cost, service network"],
         ["Price-first / emerging", "Next frontier", "Affordable, simple, durable", "Purpose-built entry models"]],
        col_widths=[2.6, 2.2, 3.8, 3.73])
    tables.takeaway_bar(s, d.theme, r[0], r[1] + 3.0, r[2],
        "The growth cohort is the pragmatic mainstream - they buy on total cost, "
        "reliability and charging, not on novelty. Design the offer for them.")

    s, r = d.content("BEV wins the long run, but PHEV is still a real bridge where charging lags - so match the powertrain offer to local charging maturity",
        body=[("BEV dominates and holds.", "Battery-electric vehicles take roughly "
               "70% of EV sales and own the structural trajectory; as charging "
               "improves and battery cost falls, the case for a combustion engine "
               "on board weakens in most use-cases."),
              ("PHEV has a real near-term role.", "In regions with sparse charging, "
               "long distances or range-anxious buyers, plug-in hybrids de-risk "
               "adoption and build the charging habit. Their share has proven more "
               "durable than many expected, particularly in markets pushing back on "
               "pure-BEV mandates."),
              ("Plan for a BEV end-state, hedge the path.", "The destination is "
               "clearly BEV-led, but the route differs by market. A challenger should "
               "not dismiss PHEV where charging lags - it can be the on-ramp that "
               "earns the customer relationship."),
              "Read the BEV/PHEV mix as a proxy for local charging maturity, and "
              "match the powertrain offer to it."],
        kicker=K(2), sources=[IEA, BNEF])
    d.chart_caption(s, r[0], r[1], r[2], "BEV vs PHEV share of EV sales", "%, global")
    charts.column(s, d.theme, r[0], r[1] + 0.55, r[2], r[3] - 0.6,
                  ["2021", "2023", "2025E"],
                  {"BEV": [71, 70, 70], "PHEV": [29, 30, 30]})

    s, r = d.content_blocks("Demand is splitting into three distinct price bands",
        blocks=[("Facts", "Three arenas are forming: a premium band that buys on "
                 "performance and brand, a mass band that buys on value and is the "
                 "main volume battleground, and an emerging entry band that buys on "
                 "affordability and simplicity. Each has different economics and "
                 "competitors."),
                ("Insights", "Margin concentrates at the top; volume and the long-run "
                 "future concentrate at the bottom. The mass band in the middle is "
                 "where the largest number of players collide and where price "
                 "competition erodes margin fastest."),
                ("Implications", "Pick a band deliberately and design the entire "
                 "model - product, platform, channel and financing - around it. The "
                 "entry band is the least contested today and the largest future "
                 "pool, but it punishes any cost indiscipline.")],
        kicker=K(2), sources=[ICCT, TRK])
    frameworks.kpi_grid(s, d.theme, r[0], r[1], r[2], r[3],
        [("Premium", "Brand & performance", "highest margin, low volume"),
         ("Mass", "Value battleground", "most contested, margin-thin"),
         ("Entry", "Affordable & simple", "largest future pool")], cols=1)

    s, r = d.content("Total cost of ownership already favours EVs, but buyers anchor on sticker price - so sell whole-life cost, financing and energy as one package",
        body=[("Sticker price still lags.", "Up-front price remains higher than a "
               "comparable combustion car in many segments, and it is the most "
               "visible, most-cited barrier for mainstream buyers who anchor on the "
               "number on the windscreen."),
              ("But whole-life cost often wins.", "Lower energy cost per kilometre "
               "and reduced maintenance - fewer moving parts, no oil changes - can "
               "make five-year total cost of ownership competitive or better, "
               "especially for high-mileage private drivers and commercial fleets."),
              ("The gap is a communication problem.", "Because buyers under-weight "
               "running costs and over-weight purchase price, the economic case is "
               "frequently real but unseen. Financing structures that spread the "
               "battery cost and bundle energy can close the perception gap."),
              "Sell total cost of ownership, financing and energy as a package, not "
              "a sticker price - it is the most reliable way to convert the "
              "pragmatic mainstream."],
        kicker=K(2), sources=[ICCT, IEA])
    d.chart_caption(s, r[0], r[1], r[2], "Illustrative 5-year cost of ownership", "Indexed, ICE = 100")
    charts.column(s, d.theme, r[0], r[1] + 0.55, r[2], r[3] - 0.6,
                  ["Purchase", "Energy", "Maintenance", "Total"],
                  {"ICE": [85, 100, 100, 100], "EV": [100, 45, 60, 92]})

    s, r = d.content_blocks("Range, charging and price stay the top barriers - but increasingly as perception, so compete on trust and education, not just on specs",
        blocks=[("Facts", "Survey after survey ranks the same three obstacles for "
                 "non-adopters: access to convenient charging, range anxiety, and "
                 "up-front price. They have been remarkably stable even as the "
                 "underlying product has improved."),
                ("Insights", "Increasingly these are perception gaps as much as real "
                 "ones. Average range and charging density now exceed the actual "
                 "daily needs of most buyers, yet the worry persists - which means "
                 "the barrier is as much psychological as technical."),
                ("Implications", "Compete on education, transparent and reliable "
                 "charging maps, guaranteed residual values and clear financing, not "
                 "only on the spec sheet. Removing the fear is often higher-leverage "
                 "than adding another 50 km of range.")],
        kicker=K(2), sources=[TRK, ICCT])
    frameworks.kpi_grid(s, d.theme, r[0], r[1], r[2], r[3],
        [("No.1", "Charging access", "real and perceived"),
         ("No.2", "Range anxiety", "gap now narrowing"),
         ("No.3", "Up-front price", "TCO offsets it"),
         ("No.4", "Residual value", "confidence gap")], cols=2)

    s, r = d.content("A used-EV market is forming and stabilising residuals - unlocking mainstream entry and making battery-health certification a trust-and-margin play",
        body=[("Residual values are stabilising.", "After a period of early "
               "volatility, used-EV values are maturing as battery-health data, "
               "standardised diagnostics and manufacturer warranties give second-hand "
               "buyers the confidence the category previously lacked."),
              ("Used supply unlocks the mainstream.", "A liquid, affordable "
               "second-hand market is how a large share of mass buyers actually enter "
               "EV ownership. It also underpins new-car residual values and therefore "
               "the economics of leasing and subscription, which drive much of new "
               "volume."),
              ("Trust is the scarce asset.", "Battery-health certification, "
               "transparent state-of-health reporting and certified-used programmes "
               "are still under-built across the industry - an opportunity to create "
               "both customer trust and a margin stream."),
              "A challenger that engineers residual value deliberately - through "
              "battery warranties and certified-used - lowers the monthly cost of "
              "its new cars and widens its addressable market."],
        kicker=K(2), sources=[TRK, BNEF])
    d.chart_caption(s, r[0], r[1], r[2], "Used-EV transactions (indexed)", "2021 = 100, illustrative")
    charts.line(s, d.theme, r[0], r[1] + 0.55, r[2], r[3] - 0.7,
                ["2021", "2022", "2023", "2024", "2025E"],
                {"Used-EV index": [100, 150, 230, 330, 460]})

    d.prose("Section 2 takeaways - demand is mainstreaming, trust is the gate", [
        ("The growth cohort buys on cost and confidence.", "Win the pragmatic "
         "mainstream with total cost of ownership, reliability and charging - not "
         "novelty. The early-adopter playbook no longer reaches the volume buyer."),
        ("Pick a price band deliberately.", "The entry band is least contested and "
         "the largest future pool; the mass band is where margin is competed away. "
         "Design the whole model around the chosen band."),
        ("Build the trust infrastructure.", "Residual guarantees, battery-health "
         "certification and certified-used programmes close the confidence gap and, "
         "done well, become a differentiated margin stream."),
    ], kicker=K(2), image_path=img("sum_demand.jpg"))

    # ================= PART 3 - COMPETITIVE LANDSCAPE =================
    d.section_divider(3, "Competitive landscape",
                      "Share, business-model archetypes, China, and the supply chain",
                      ["Share is concentrating around a few scaled players, because EV economics reward scale - so reach scale in one lane quickly, or partner for it",
                       "Two archetypes lead - integration and cost leadership - and straddling both leaves you sub-scale on each, so margin follows focus",
                       "Profile - the integrator model",
                       "Profile - the cost-leader model",
                       "Chinese OEMs are resetting the global cost frontier and accelerating exports - so assume the frontier is set in China and plan local content",
                       "Legacy OEMs are strong in brand and scale but short on software - so expect partnerships, and a software-layer opening for challengers to take",
                       "The battery supply chain is the real moat - whoever controls the midstream owns EV cost, and therefore margin and supply security",
                       "Software-defined vehicles open a new front"],
                      takeaway="Scale, battery control and software - not legacy brand "
                               "alone - now decide who wins.",
                      image_path=img("div_competition.jpg"))

    s, r = d.content("Share is concentrating around a few scaled players, because EV economics reward scale - so reach scale in one lane quickly, or partner for it",
        body=[("Scale is pulling away.", "A handful of OEMs that combine battery "
               "control, fast product cycles and software depth are taking a rising "
               "share of global EV volume, while the long tail of sub-scale players "
               "struggles to match their cost and cadence."),
              ("The economics are unforgiving.", "EVs reward scale in cells, "
               "platforms and software amortisation. Without captive supply or a "
               "differentiated software stack, a small player faces higher unit cost "
               "and slower product refresh - a structurally losing position in a "
               "price-competitive market."),
              ("Partnership is the scale shortcut.", "For challengers, alliances on "
               "cells, platforms and charging are increasingly the way to borrow the "
               "scale they cannot build alone - a recurring pattern among new "
               "entrants and transitioning incumbents alike."),
              "Reach minimum efficient scale in one chosen lane quickly, or secure it "
              "through partnership - drifting at sub-scale across several lanes is the "
              "most common way to lose."],
        kicker=K(3), sources=[OICA, FILE])
    d.chart_caption(s, r[0], r[1], r[2], "Illustrative EV unit share by maker", "%, 2025E")
    charts.bar(s, d.theme, r[0], r[1] + 0.55, r[2], r[3] - 0.7,
               ["Leader A", "Leader B", "Maker C", "Maker D", "Others"],
               [19, 17, 11, 8, 45], highlight_idx=0)

    s, r = d.wide_slide("Two archetypes lead - integration and cost leadership - and straddling both leaves you sub-scale on each, so margin follows focus",
        kicker=K(3), sources=[FILE, TRK])
    tables.table(s, d.theme, r[0], r[1], r[2], 2.85,
        [["Dimension", "Integrator", "Cost leader", "Challenger (you)"],
         ["Core move", "In-house cells + owned OS/OTA + direct sales",
          "Captive battery supply + broad price ladder", "Pick one lane; do not straddle"],
         ["Edge", "Premium brand, software margin", "Volume, price, speed", "Focus and cadence"],
         ["Margin source", "Software, services, brand", "Scale, supply control", "Niche depth"],
         ["Main risk", "Capital intensity", "Margin compression in price wars", "Sub-scale if unfocused"]],
        col_widths=[1.9, 3.7, 3.5, 3.23])
    tables.takeaway_bar(s, d.theme, r[0], r[1] + 3.0, r[2],
        "Do not straddle. Win one lane - integration OR cost - reach scale, then "
        "extend. Margin follows focus, and focus is the scarce discipline.")

    s, r = d.content("The integrator wins margin through stack control and software - so a challenger should own the software and direct customer relationship early",
        body=[("Owns the full stack.", "The integrator brings cells, software and "
               "direct sales in-house, capturing margin across hardware, software and "
               "the ongoing customer relationship rather than ceding it to suppliers "
               "and dealers."),
              ("Brand and cadence command price.", "A strong brand combined with a "
               "relentless cadence of over-the-air feature updates sustains premium "
               "pricing and a high attach rate of paid software - a recurring revenue "
               "stream the rest of the industry struggles to match."),
              ("The risk is capital and tempo.", "The model is capital-intensive and "
               "demands continuous product and software speed to justify the premium; "
               "any slip in cadence quickly erodes the price advantage."),
              "The durable, transferable lessons for a challenger are the owned "
              "software platform and the direct customer relationship - buy or build "
              "them early, even on partnered hardware."],
        kicker=K(3), sources=[FILE])
    tables.table(s, d.theme, r[0], r[1] + 0.2, r[2], 2.5,
        [["Lever", "Integrator approach"],
         ["Battery", "In-house or JV cells"],
         ["Software", "Owned OS + OTA + paid features"],
         ["Channel", "Direct-to-consumer"],
         ["Margin", "Highest, software-led"]],
        col_widths=[1.9, 4.2])

    s, r = d.content("The cost leader wins on scale and captive battery supply - so without captive supply, a challenger must differentiate rather than fight on price",
        body=[("Owns the cost curve.", "Control of battery supply and a broad price "
               "ladder let the cost leader undercut on price while protecting margin, "
               "turning cost into the primary weapon and forcing every rival to "
               "respond on its terms."),
              ("Speed compounds the advantage.", "Fast product cycles and deep "
               "vertical integration compress both cost and time-to-market versus "
               "legacy peers, so the gap widens with each model generation rather "
               "than closing."),
              ("The risk is the price war it starts.", "Aggressive pricing and "
               "overcapacity can compress margins across the entire segment, "
               "including the cost leader's own - a war that is easier to start than "
               "to end."),
              "For a challenger without captive supply, competing head-on with the "
              "cost leader on price is a losing fight; differentiation on software, "
              "experience or a niche is the only defensible response."],
        kicker=K(3), sources=[FILE, OICA])
    tables.table(s, d.theme, r[0], r[1] + 0.2, r[2], 2.5,
        [["Lever", "Cost-leader approach"],
         ["Battery", "Captive supply chain"],
         ["Software", "Good-enough, improving fast"],
         ["Channel", "Broad, multi-tier"],
         ["Margin", "Scale- and supply-led"]],
        col_widths=[1.9, 4.2])

    s, r = d.content("Chinese OEMs are resetting the global cost frontier and accelerating exports - so assume the frontier is set in China and plan local content",
        body=[("A new cost benchmark.", "Chinese OEMs combine battery control, "
               "remarkably rapid product cycles and aggressive price ladders. The "
               "result is a cost and price benchmark that every other player - "
               "incumbent or challenger - is now measured against, wherever they "
               "operate."),
              ("Export is accelerating.", "Rising export volumes are reshaping "
               "Europe and emerging markets and have already prompted tariff and "
               "local-content responses. The competitive pressure is no longer "
               "contained to the home market."),
              ("Localisation is the counter-move.", "For incumbents and challengers, "
               "the response is some mix of local production to meet content rules, "
               "differentiation on software and service, and partnership on cells - "
               "matching China on price alone is rarely viable."),
              "Assume the cost frontier is set in China and plan differentiation, "
              "local content and supply strategy from that premise, not against an "
              "outdated cost base."],
        kicker=K(3), sources=[OICA, ICCT])
    d.chart_caption(s, r[0], r[1], r[2], "Illustrative China EV exports", "Units, millions")
    charts.column(s, d.theme, r[0], r[1] + 0.55, r[2], r[3] - 0.6,
                  ["2021", "2022", "2023", "2024", "2025E"],
                  {"Exports (m)": [0.5, 1.0, 1.7, 2.2, 2.6]}, highlight=(0, 4))

    s, r = d.content_blocks("Legacy OEMs are strong in brand and scale but short on software - so expect partnerships, and a software-layer opening for challengers to take",
        blocks=[("Facts", "Incumbents carry combustion-engine margin, large dealer "
                 "networks and established labour structures that complicate a fast "
                 "EV pivot. Many have reset or softened their EV timelines as early "
                 "losses mounted and demand growth cooled."),
                ("Insights", "Their genuine advantages are brand, distribution reach "
                 "and manufacturing scale; their binding constraints are software "
                 "depth and a cost structure built for a different powertrain. The "
                 "transition is as much organisational as technical."),
                ("Implications", "Expect a wave of partnerships - on cells, software "
                 "and platforms - and selective retreat from unprofitable segments. A "
                 "challenger can win precisely the software and customer-experience "
                 "layer that incumbents find hardest to build.")],
        kicker=K(3), sources=[FILE, TRK])
    frameworks.kpi_grid(s, d.theme, r[0], r[1], r[2], r[3],
        [("Asset", "Brand & dealers", "still a real strength"),
         ("Asset", "Manufacturing scale", "decades of capability"),
         ("Gap", "Software depth", "the hardest to close"),
         ("Gap", "Cost structure", "legacy overhang")], cols=2)

    s, r = d.wide_slide("The battery supply chain is the real moat - whoever controls the midstream owns EV cost, and therefore margin and supply security",
        kicker=K(3), sources=[BNEF, IRENA])
    frameworks.chevron(s, d.theme, r[0], r[1] + 0.4, r[2], 0.8,
        ["Raw materials", "Refining", "Cells", "Packs", "Vehicle", "Recycling"],
        captions=["Lithium, nickel, cobalt, graphite - concentrated supply",
                  "Midstream led by a few countries - a choke point",
                  "Scale and chemistry know-how decide cost",
                  "Integration with the vehicle platform",
                  "Where brand and experience add value",
                  "Closing the loop; second-life and security"])
    tables.takeaway_bar(s, d.theme, r[0], r[1] + 3.0, r[2],
        "Control or secure the midstream (refining and cells). Whoever owns the "
        "battery value chain owns EV cost - and therefore the margin and the supply security.")

    s, r = d.content_blocks("Software-defined vehicles open a new, high-margin front - so treat the car as a platform and earn recurring margin even on competitive hardware",
        blocks=[("Facts", "Vehicle value is migrating to the software layer: "
                 "over-the-air updates, advanced driver assistance, infotainment and "
                 "paid feature subscriptions now drive a growing share of both "
                 "perceived value and gross margin."),
                ("Insights", "Software is high-margin, recurring and decouples value "
                 "from the metal - the same hardware can be upgraded and monetised "
                 "over its life. It is also the moat legacy players find hardest to "
                 "build and the layer that deepens the customer and data relationship."),
                ("Implications", "Treat the vehicle as a platform, not a product. A "
                 "challenger can differentiate and earn recurring margin on software "
                 "even on competitive hardware - and the data loop compounds the "
                 "advantage over time.")],
        kicker=K(3), sources=[FILE, TRK])
    frameworks.kpi_grid(s, d.theme, r[0], r[1], r[2], r[3],
        [("OTA", "Over-the-air", "value after the sale"),
         ("ADAS", "Driver assistance", "premium attach today"),
         ("Apps", "In-car services", "ecosystem lock-in"),
         ("Data", "Fleet data loop", "new, compounding margin")], cols=2)

    d.prose("Section 3 takeaways - scale, battery and software decide the winners", [
        ("Reach scale in one lane.", "Integration or cost - straddling both leaves "
         "you sub-scale on each. Choose, commit, and use partnership to borrow the "
         "scale you cannot build."),
        ("Secure the battery value chain.", "Control of cells and the midstream is "
         "the real cost moat and a supply-security imperative; without it, do not "
         "try to compete on price."),
        ("Win the software layer.", "Recurring, high-margin and the hardest gap for "
         "incumbents to close - the single most defensible place for a challenger to "
         "build durable advantage."),
    ], kicker=K(3), image_path=img("sum_competition.jpg"))

    # ================= PART 4 - TECHNOLOGY & TRENDS =================
    d.section_divider(4, "Technology & trends",
                      "Batteries, charging, software and autonomy",
                      ["Battery chemistry is bifurcating: LFP volume vs high-nickel",
                       "Solid-state is a step-change - but later than the hype",
                       "Charging is getting faster and smarter",
                       "Software and OTA become the product",
                       "Autonomy advances in levels, not leaps - so win the assisted-driving present for premium attach, and treat full autonomy as optionality",
                       "Vehicle-to-grid links EVs to the energy system"],
                      takeaway="Technology is commoditising the powertrain and moving "
                               "value to chemistry control, software and energy services.",
                      image_path=img("div_technology.jpg"))

    s, r = d.wide_slide("Battery chemistry is bifurcating by use-case, making chemistry a strategic choice - LFP for entry and fleets, high-nickel for premium range",
        kicker=K(4), sources=[BNEF, IRENA])
    tables.table(s, d.theme, r[0], r[1], r[2], 2.85,
        [["Chemistry", "Relative cost", "Energy density", "Best for", "Trajectory"],
         ["LFP", "Lowest", "Moderate", "Mass / entry cars, fleets, storage", "Share rising fast"],
         ["High-nickel (NMC)", "Higher", "Highest", "Premium, long-range vehicles", "Stable, premium niche"],
         ["Sodium-ion", "Very low (potential)", "Lower", "Entry cars, stationary storage", "Early - one to watch"],
         ["Solid-state", "High (today)", "Very high", "Future premium / long-range", "Late-decade at scale"]],
        col_widths=[2.5, 2.2, 2.1, 3.2, 2.33])
    tables.takeaway_bar(s, d.theme, r[0], r[1] + 3.0, r[2],
        "Match chemistry to band: LFP for entry, mass and fleets; high-nickel for "
        "premium range. Chemistry is now a strategic choice, not just a technical one.")

    s, r = d.content("Solid-state is a real step-change but later than the hype - so treat it as optionality and build the plan on today's LFP-led affordability wave",
        body=[("The prize is genuinely large.", "Solid-state batteries promise "
               "higher energy density, faster charging and improved safety - "
               "potentially resetting the range and charging trade-offs that still "
               "shape buyer perception today."),
              ("But timelines keep slipping.", "Manufacturing at automotive scale and "
               "cost remains unproven, and repeated delays have pushed credible "
               "high-volume production to the latter part of the decade. The "
               "engineering and the cost curve are both unfinished."),
              ("Over-indexing on it is a trap.", "Betting the strategy on solid-state "
               "risks missing the LFP-led affordability wave that is creating volume "
               "right now. The near-term game is won on cheaper cells, not on a "
               "next-generation chemistry that is not yet shipping."),
              "Track solid-state as strategic optionality - fund a watching brief and "
              "partnerships - but build the plan on the chemistries available today."],
        kicker=K(4), sources=[BNEF])
    d.chart_caption(s, r[0], r[1], r[2], "Illustrative energy density by chemistry", "Wh/kg, indexed")
    charts.bar(s, d.theme, r[0], r[1] + 0.55, r[2], r[3] - 0.7,
               ["LFP", "NMC", "Solid-state (target)"], [100, 135, 180],
               highlight_idx=2)

    s, r = d.content("Charging is getting faster, denser and smarter - turning it from a cost into a branded, recurring-revenue service and a purchase driver",
        body=[("Peak speeds keep rising.", "High-power DC charging is steadily "
               "cutting stop-times, easing the long-distance use-case that worries "
               "prospective buyers most. The headline kilowatt figure, however, "
               "matters less than real-world reliability and queue times."),
              ("Smart charging is the bigger prize.", "Managed and bidirectional "
               "charging shifts load away from peaks, lowers the cost of energy and "
               "can support the grid - turning charging from a pure cost into a "
               "service with its own revenue and a grid-balancing role."),
              ("Experience becomes a brand battleground.", "Speed, reliability and "
               "frictionless payment increasingly shape brand perception and "
               "repurchase. A poor charging experience undermines an otherwise strong "
               "vehicle; a great one becomes a reason to buy."),
              "For a challenger, a credible charging and energy-services proposition "
              "is both a purchase driver and a recurring-revenue opportunity."],
        kicker=K(4), sources=[IRENA, IEA])
    d.chart_caption(s, r[0], r[1], r[2], "Illustrative peak charge power", "kW, typical fast charger")
    charts.line(s, d.theme, r[0], r[1] + 0.55, r[2], r[3] - 0.7,
                ["2018", "2020", "2022", "2024", "2026E"],
                {"Peak kW": [50, 120, 200, 270, 350]})

    s, r = d.content_blocks("Software and OTA increasingly are the product, decoupling value from the metal - so invest in the platform and data loop that compound over time",
        blocks=[("Facts", "Over-the-air updates, advanced driver assistance and paid "
                 "software features now drive a rising share of both perceived value "
                 "and gross margin, and a growing portion of post-sale revenue."),
                ("Insights", "Software decouples value from the metal: the same "
                 "hardware can be improved, monetised and differentiated across its "
                 "life. That changes the business model from a one-time sale to an "
                 "ongoing relationship - and a data advantage that compounds."),
                ("Implications", "Invest in a genuine software platform and the data "
                 "loop behind it; it is the most durable, highest-margin layer a "
                 "challenger can own, and it can differentiate even competitive "
                 "hardware in a commoditising market.")],
        kicker=K(4), sources=[FILE, TRK])
    frameworks.kpi_grid(s, d.theme, r[0], r[1], r[2], r[3],
        [("OTA", "Continuous upgrade", "value after the sale"),
         ("Pay", "Paid software", "recurring margin"),
         ("UX", "In-car experience", "brand differentiator"),
         ("Data", "Closed loop", "improves the whole fleet")], cols=2)

    s, r = d.content("Autonomy advances in levels, not leaps - so win the assisted-driving present for premium attach, and treat full autonomy as optionality",
        body=[("Assistance is mainstreaming.", "Level-2 and 2+ driver assistance is "
               "spreading quickly and is a premium attach today; it improves safety, "
               "eases the driving task and raises willingness to pay - a tangible "
               "near-term value driver."),
              ("Full autonomy stays gated.", "Higher levels remain constrained by "
               "regulation, liability and the long tail of edge-case reliability. "
               "Robotaxi pilots advance in narrow geographies, but broad private "
               "ownership of fully autonomous cars is a longer arc than headlines "
               "imply."),
              ("Compete on the present, option the future.", "The pragmatic move is "
               "to offer excellent assisted-driving now and bank the premium attach, "
               "while treating full autonomy as optionality rather than a near-term "
               "differentiator to build the business on."),
              "Assisted driving is where willingness-to-pay and feasibility overlap "
              "today; that is where a challenger should concentrate effort."],
        kicker=K(4), sources=[ICCT, TRK])
    d.chart_caption(s, r[0], r[1], r[2], "Illustrative ADAS attach rate", "% of new EVs")
    charts.column(s, d.theme, r[0], r[1] + 0.55, r[2], r[3] - 0.6,
                  ["2021", "2023", "2025E"], {"L2+ attach %": [22, 38, 55]},
                  highlight=(0, 2))

    d.prose("Section 4 takeaways - value moves off the powertrain", [
        ("Chemistry is a strategy choice.", "LFP for affordability, mass and fleets; "
         "high-nickel for premium range; solid-state as late-decade optionality. "
         "Build the plan on chemistries shipping today."),
        ("Charging and software are the new arenas.", "Both are recurring-revenue, "
         "experience-led battlegrounds and increasingly the basis of differentiation "
         "- not afterthoughts bolted onto a vehicle."),
        ("Autonomy - win the assisted-driving present.", "Bank the premium attach "
         "from Level-2+ now and treat full autonomy as an option, not the foundation "
         "of the strategy."),
    ], kicker=K(4), image_path=img("sum_technology.jpg"))

    # ============== PART 5 - OPPORTUNITIES & STRATEGY ==============
    d.section_divider(5, "Opportunities & strategy",
                      "Where the next decade is won - and what to do about it",
                      ["Four opportunity spaces emerge below and around the vehicle - so aim where attractiveness and your right-to-win overlap, not at the biggest number",
                       "Opportunity 1 - the affordable / entry segment",
                       "Opportunity 2 - the software & services margin pool",
                       "Opportunity 3 - emerging markets and small mobility grow fastest on different economics - a locally-partnered, affordable model can build an early lead",
                       "Strategic options for a challenger",
                       "Implications for a new entrant - focus beats breadth, so commit to one lane, secure its scarce input, and sequence expansion from a defensible base"],
                      takeaway="The biggest, least-contested pools are affordability, "
                               "software/services and the upstream value chain.",
                      image_path=img("div_opportunity.jpg"))

    s, r = d.content_blocks("Four opportunity spaces emerge below and around the vehicle - so aim where attractiveness and your right-to-win overlap, not at the biggest number",
        blocks=[("Facts", "Screening the market surfaces four distinct opportunity "
                 "spaces: genuinely affordable vehicles, software and services, "
                 "emerging-market mobility, and the battery and charging value chain. "
                 "Each has a different size, growth rate and right-to-win."),
                ("Insights", "The premium and mass new-car bands are crowded and "
                 "margin-thin. The open pools sit below the vehicle (affordability) "
                 "and around it (software, supply, charging) - exactly where most "
                 "incumbents are least well positioned."),
                ("Implications", "Aim where market attractiveness and your own "
                 "right-to-win overlap, not simply at the biggest number. The "
                 "discipline is to say no to large but unwinnable arenas and commit "
                 "to a smaller one you can actually own.")],
        kicker=K(5), sources=[IEA, TRK])
    frameworks.kpi_grid(s, d.theme, r[0], r[1], r[2], r[3],
        [("1", "Affordable / entry", "largest future pool"),
         ("2", "Software & services", "highest, recurring margin"),
         ("3", "Emerging markets", "fastest growth"),
         ("4", "Battery & charging", "the cost and supply moat")], cols=2)

    s, r = d.content("Opportunity 1 - own the affordable / entry segment: the least-contested, largest future pool, now viable on LFP but only with real cost discipline",
        body=[("It is the least-contested pool.", "Most players still cluster in the "
               "premium and mass bands, leaving the sub-band of genuinely affordable "
               "EVs relatively open - even though it represents the largest pool of "
               "future volume as the market mainstreams."),
              ("LFP makes it viable for the first time.", "Low-cost chemistry, "
               "simplified platforms and manufacturing learning have made a "
               "profitable entry-segment model realistic where it previously was "
               "not. The economics now work if the cost discipline is real."),
              ("It demands a purpose-built model.", "Winning here means designing the "
               "whole offer - product, platform, channel and financing - around the "
               "entry buyer, rather than de-contenting a premium car, which carries "
               "the wrong cost base and the wrong complexity."),
              "The entry band rewards relentless cost discipline and punishes "
              "indulgence; it is a different operating model, not a cheaper version "
              "of the existing one."],
        kicker=K(5), sources=[ICCT, BNEF])
    d.chart_caption(s, r[0], r[1], r[2], "Illustrative volume pool by band", "Share of 2030E units")
    charts.doughnut(s, d.theme, r[0], r[1] + 0.55, r[2] - 0.4, r[3] - 0.7,
                    ["Entry", "Mass", "Premium"], [40, 42, 18], highlight_idx=0)

    s, r = d.content("Opportunity 2 - capture the software & services margin pool, where durable profit is migrating and a challenger can win even on partnered hardware",
        body=[("Margin is migrating here.", "As hardware commoditises and the "
               "powertrain price penalty disappears, recurring software, charging and "
               "service revenue become the durable profit pool. The metal increasingly "
               "earns less; what runs on it earns more."),
              ("It compounds over the life of the car.", "Software margin recurs "
               "year after year and deepens the customer relationship and the data "
               "advantage, which in turn improves the product - a flywheel that a "
               "one-time hardware sale cannot match."),
              ("It is winnable even on partnered hardware.", "A challenger does not "
               "need to win on the vehicle to win on software, experience and an "
               "energy or charging-services bundle - the layer where incumbents are "
               "weakest and where differentiation is most defensible."),
              "Treat software and services as a primary business, not an accessory to "
              "the car; it is where the next decade's profit concentrates."],
        kicker=K(5), sources=[FILE, TRK])
    d.chart_caption(s, r[0], r[1], r[2], "Illustrative profit pool mix", "% of sector profit")
    charts.column(s, d.theme, r[0], r[1] + 0.55, r[2], r[3] - 0.6,
                  ["Hardware", "Software", "Services", "Charging"],
                  {"2025E": [70, 12, 10, 8], "2030E": [50, 22, 16, 12]})

    s, r = d.content("Opportunity 3 - emerging markets and small mobility grow fastest on different economics - a locally-partnered, affordable model can build an early lead",
        body=[("Fastest growth, low base.", "Emerging markets grow fastest off a low "
               "base, and the entry point is frequently electric two- and "
               "three-wheelers and urban fleets rather than passenger cars - a "
               "different product and a different customer."),
              ("Different economics apply.", "Affordability, accessible financing and "
               "basic charging access matter far more than premium features, and "
               "local partnerships for distribution and service are often decisive in "
               "ways they are not in mature markets."),
              ("Early position is durable.", "A right-sized, affordable, "
               "locally-partnered offer can establish an early lead and brand habit "
               "before the market premiumises - a foothold that is hard for later "
               "entrants to dislodge."),
              "These markets reward a purpose-built, locally-partnered model and "
              "patient brand-building, not a premium product imported unchanged."],
        kicker=K(5), sources=[IEA, IRENA])
    d.chart_caption(s, r[0], r[1], r[2], "Illustrative EV growth by region", "Index, 2025E = 100 to 2030E")
    charts.bar(s, d.theme, r[0], r[1] + 0.55, r[2], r[3] - 0.7,
               ["Emerging", "China", "Europe", "N. America"], [320, 180, 165, 175],
               highlight_idx=0)

    s, r = d.wide_slide("Strategic options for a challenger - three viable lanes; pick one as the spearhead and one as the hedge, because focus beats breadth",
        kicker=K(5), sources=[TRK, FILE])
    tables.table(s, d.theme, r[0], r[1], r[2], 2.85,
        [["Option", "Where to play", "How to win", "What it needs", "Main risk"],
         ["A. Entry disruptor", "Affordable band", "Low-cost LFP platform + financing",
          "Cost discipline, secured supply", "Margin thinness"],
         ["B. Software-first", "Across bands", "Own OS, OTA and services",
          "Software talent, data loop", "Reliance on hardware partner"],
         ["C. Value-chain play", "Battery / charging", "Secure midstream or network",
          "Capital, partnerships", "High capital intensity"]],
        col_widths=[2.2, 2.2, 3.3, 2.6, 2.03])
    tables.takeaway_bar(s, d.theme, r[0], r[1] + 3.0, r[2],
        "Pick one lane as the spearhead and a second as the hedge - A or B is the "
        "most capital-efficient entry for most challengers.")

    s, r = d.content_blocks("Implications for a new entrant - focus beats breadth, so commit to one lane, secure its scarce input, and sequence expansion from a defensible base",
        blocks=[("Facts", "The crowded, margin-thin arenas are the premium and mass "
                 "new-car bands. The open pools are affordability, software and "
                 "services, and the upstream battery and charging value chain."),
                ("Insights", "A challenger wins through depth in one lane and a clear "
                 "right-to-win, not by competing everywhere at sub-scale. The most "
                 "common failure mode is spreading scarce capital and talent too "
                 "thin to be excellent at anything."),
                ("Implications", "Commit to one spearhead lane, secure the scarce "
                 "input it needs - cost discipline and supply, or software talent and "
                 "data - and sequence expansion from a defensible base, borrowing "
                 "scale through partnership where it makes sense.")],
        kicker=K(5), sources=[TRK])
    frameworks.kpi_grid(s, d.theme, r[0], r[1], r[2], r[3],
        [("Focus", "One lane first", "depth beats breadth"),
         ("Secure", "The scarce input", "cost-supply or software"),
         ("Sequence", "Expand from a base", "win, then extend"),
         ("Partner", "Borrow scale", "cells, platform, charging")], cols=2)

    # ============================ CLOSING ============================
    d.conclusion("Back to the three questions - our desk-research view",
        ["Growth is real but maturing - plan for a mainstream market by 2030, "
         "carried by affordability and charging, not subsidy.",
         "Two models win - integration and cost; a challenger must pick one lane "
         "and reach scale, not straddle both.",
         "The opportunity is below and around the vehicle - affordability, software "
         "and services, and the battery and charging value chain.",
         "So what: choose one spearhead lane, secure its scarce input, and win a few "
         "concentrated, driver-fit markets before extending."],
        sources=[IEA, FILE])

    d.prose("Recommended priorities - sequence and no-regret moves", [
        ("Now (0-12 months).", "Choose the spearhead lane - entry-disruptor or "
         "software-first; lock a battery or cell partnership to secure supply and "
         "cost; and stand up a real software and data platform from day one."),
        ("Next (12-24 months).", "Launch a focused hero product in the chosen band; "
         "build the charging and financing bundle that converts mainstream buyers; "
         "and enter two or three driver-fit markets rather than spreading thin."),
        ("Later (24 months+).", "Extend into adjacent bands from the defensible "
         "base; scale software and services attach to grow recurring margin; and "
         "evaluate selective value-chain integration where it protects cost."),
        ("No-regret moves.", "Regardless of lane: invest in software talent, secure "
         "battery supply, and build residual-value and trust programmes - all three "
         "pay off under every scenario."),
    ], kicker="Strategy", columns=2)

    d.source_list("Methodology & sources", {
        "Approach": [("Layered desk research - facts, then insights, then "
                      "implications; every figure traceable to a source; conflicting "
                      "sources reconciled and dated; estimates marked", "")],
        "Market & policy": [IEA, ICCT, IRENA],
        "Competition & finance": [OICA, FILE, BNEF],
        "Notes": [("All figures rounded / illustrative for a public demo - validate "
                   "against primary licensed sources before any decision", ""),
                  ("Forward years marked 'E'; this is a desk-research view, not a "
                   "forecast model", "")],
    }, kicker="Methodology")

    d.prose("Glossary", [
        ("BEV / PHEV.", "Battery-electric vehicle (no engine) / plug-in hybrid "
         "electric vehicle (battery plus a combustion engine as backup)."),
        ("TCO.", "Total cost of ownership - purchase price plus energy, maintenance "
         "and depreciation across the life of the vehicle."),
        ("LFP / NMC.", "Lithium-iron-phosphate (lower cost, durable) and "
         "nickel-manganese-cobalt (higher energy density) battery chemistries."),
        ("OTA.", "Over-the-air - software updates and new features delivered "
         "remotely to the vehicle, without a workshop visit."),
        ("ADAS.", "Advanced driver-assistance systems, for example Level-2/2+ "
         "assisted driving (lane-keeping, adaptive cruise)."),
        ("V2G.", "Vehicle-to-grid - bidirectional charging that lets an EV feed "
         "power back to support the electricity grid."),
        ("Midstream.", "The battery value-chain steps between raw materials and the "
         "vehicle: refining of materials and cell/pack manufacturing."),
        ("Parc.", "The total installed base of vehicles in use in a market."),
    ], columns=2)

    d.back_cover("Thank you", "Acme Research  -  Desk-research practice  -  2026")

    path = d.save(os.path.join(OUT, "ev_market.pptx"))
    print(f"Built {d.page} slides -> {path}")
    return path


if __name__ == "__main__":
    build()
