# Bleed App — Onboarding Research & Blueprint

## Where to Find Real Onboarding Screenshots

These sites have actual step-by-step screenshot flows you can study. Not generic galleries — real teardowns.

### Best for Your Use Case (Health/Period Tracker)

| Site | What You Get | Direct Link |
|------|-------------|-------------|
| **App Fuel** | 32 screens of Flo's onboarding + 17 screens of Clue's — free screenshot galleries | [Flo](https://www.theappfuel.com/examples/flo_onboarding), [Clue](https://www.theappfuel.com/examples/clue_onboarding) |
| **App Fuel — All Onboarding** | 146 app onboarding flows with screenshots. Filter: Flo, Clue, Calm, Headspace, BetterMe, Fitbod, Sweat, MyFitnessPal | [Browse all](https://www.theappfuel.com/flows/onboarding) |
| **Reteno Gallery** | 8,000+ real onboarding screens. Has Flo (57 screens), YAZIO, Sweat, Welltory, Cronometer | [Flo](https://gallery.reteno.com/flows/app-screens-flo), [Gallery home](https://gallery.reteno.com) |
| **UserOnboard** | Annotated teardowns — every screen gets commentary on what works/doesn't. The OG resource. | [Teardowns](https://www.useronboard.com/user-onboarding-teardowns/) |
| **Growth.Design** | Comic-style UX case studies (Superhuman, Tinder, Airbnb, Trello). Shows psychology behind each screen. | [Case studies](https://growth.design/case-studies) |

### Competitors to Study First
- **Flo** — 32-57 screens depending on source. The gold standard for period tracker onboarding. Heavy personalization.
- **Clue** — 17 screens. Simpler, more direct flow.
- **Calm** — 9 screens. Masterclass in minimal onboarding with personalization.
- **Headspace** — Conversational question flow instead of static forms.

---

## The Onboarding Blueprint for Bleed

Based on research across all sources. Adapted for a privacy-first period tracker.

### The Structure (7-12 Screens)

Bleed should be shorter than Flo (32+ screens is too much for a privacy-focused app that doesn't need server-side data). But longer than Calm (9 screens) because period tracking needs some personalization.

```
PHASE 1: Hook (Screens 1-2)
├── Welcome + value prop (privacy angle = instant differentiation)
└── "What brings you here?" (period tracking / cycle awareness / TTC / just curious)

PHASE 2: Personalize (Screens 3-6)
├── Last period date (or "I don't remember" option)
├── Typical cycle length (with "I don't know" option)
├── What do you want to track? (mood, symptoms, flow, energy, etc.)
└── Notification preferences (gentle — "Want a heads up before your period?")

PHASE 3: Privacy Moment (Screen 7)
└── The Bleed differentiator — show that data stays on device
    (This is your "aha moment" — make it visual, make it bold)

PHASE 4: Activate (Screens 8-9)
├── Show the app with their data pre-filled
└── First interaction — log something right now
```

### What the Research Says Works

**1. Get to value in under 60 seconds**
- 77% of users drop off within 3 days
- 74% abandon if onboarding is too complicated
- iOS Day 1 retention: only 25.6%

**2. Ask smart questions, not many questions**
- Flo asks 26+ questions — but it works because each feels relevant
- Bleed doesn't need that many because you're not sending data to a server
- Every question should either personalize the experience OR make the user feel understood
- "I don't know" should always be an option

**3. Delay signup / don't require it**
- Bleed stores data locally — you may not even need an account
- This is a MASSIVE advantage. Let them use the app immediately.
- DoorDash, Duolingo, Masterclass all let users explore before requiring signup

**4. Personalize the paywall (if you have one)**
- Position paywall at END of onboarding, never the beginning
- Show what they'll get based on their answers
- Fastic, Blinkist both show personalized results before pricing
- Always use soft paywalls (can dismiss/close)

**5. Make permissions feel earned**
- Don't ask for notifications on screen 1
- Apple HIG: "Give people time to start enjoying your app before making permission requests"
- Ask after you've shown value: "Want a reminder 2 days before your period?"

**6. The privacy screen IS your aha moment**
- Most apps' "aha moment" = first value delivery
- Bleed's "aha moment" = the realization your data never leaves your phone
- Make this screen visual and bold, not legal/corporate
- This is what makes someone tell their friend about the app

### What to Avoid

| Mistake | Why It Fails | What Bleed Should Do Instead |
|---------|-------------|------------------------------|
| Feature tour slides | 80% of users skip them | Show features in context, not a slideshow |
| Asking for permissions first | Kills trust before value | Ask after demonstrating value |
| Too many screens | 74% abandon complex onboarding | 7-12 screens max |
| Generic welcome | Feels like every other app | Lead with the privacy angle — nobody else does |
| Forcing account creation | Biggest friction point | Bleed doesn't need accounts — lean into this |
| Paywall before value | Churn spikes immediately | Show personalized value first, then offer premium |
| Static text-heavy screens | Nobody reads | Interactive, one question per screen |

### Apple HIG Key Rules
Source: [Apple Human Interface Guidelines — Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding)

- Get to the action quickly — avoid splash screens, menus, and instructions
- Let people dive right in
- Design for the majority — let power users adjust settings later
- Provide a way to skip tutorials and never show them to returning users
- Learning by doing > reading instructions

---

## Screen-by-Screen Patterns From Top Apps

### Flo (32 screens — period tracker)
1. Welcome screen with logo
2. "What brings you here?" (Track periods / Get pregnant / Track pregnancy)
3. Birth year
4. Goal selection deepens based on answer
5. Last period start date
6. Typical cycle length
7. Period length
8. Symptoms they experience
9. Health conditions
10. Birth control type
11. Lifestyle questions
12. ...continues with increasingly specific health questions
13. Personalized dashboard preview
14. Account creation (email/social)
15. Notification permissions

**Takeaway for Bleed:** Flo's flow works because every question feels like it's building something FOR you. But 32 screens is too long for a privacy-first app. Take the personalization concept, cut the server-dependent questions.

### Calm (9 screens — meditation)
1. Beautiful visual welcome
2. "What brings you to Calm?" (multi-select goals)
3. Experience level
4. Preferred session length
5. Attribution ("How did you hear about us?")
6. Personalized home screen preview
7. Account creation
8. Notification ask
9. Premium offer

**Takeaway for Bleed:** Calm proves you can personalize in under 10 screens. The goal question + experience level is enough to make the app feel custom.

### Duolingo (5 screens before value)
1. Language selection
2. First lesson immediately (no signup)
3. Streak commitment
4. Account creation
5. Notifications

**Takeaway for Bleed:** The "use before signup" pattern. Bleed should let users log their first period data before asking for anything.

### BetterMe Fitness (26 questions)
1. Goal selection with visuals
2. Body type selection (illustrated)
3. Target areas
4. Activity level
5. Age, weight, height
6. ...continues through personalization
7. Loading animation ("Building your plan...")
8. Personalized plan preview
9. Paywall with trial

**Takeaway for Bleed:** The "building your plan" loading screen creates anticipation. Bleed could do: "Setting up your cycle tracker..." with a privacy animation showing data staying on device.

---

## Retention Benchmarks

| Metric | Industry Average |
|--------|-----------------|
| Day 1 retention (iOS) | 25.6% |
| Day 30 retention | 3.4% |
| Users who abandon after 1 use | 25% |
| Users lost within first week | 90% |
| Onboarding completion boost to retention | +50% |
| Personalized onboarding → feature adoption | +42% |
| Social login → completion rate boost | +60% |
| Users who consider onboarding key to subscribing | 63% |

---

## Sources

- [App Fuel — Onboarding Flows](https://www.theappfuel.com/flows/onboarding) — 146 app onboarding screenshot galleries
- [Reteno Gallery](https://gallery.reteno.com) — 8,000+ onboarding screens
- [Reteno — Onboarding That Works](https://reteno.com/blog/won-in-60-seconds-how-top-apps-nail-onboarding-to-drive-subscriptions) — Best practices + 5 mistakes
- [UserOnboard](https://www.useronboard.com/user-onboarding-teardowns/) — Annotated teardowns
- [Growth.Design](https://growth.design/case-studies) — 60+ UX case studies
- [Plotline — Mobile App Onboarding Examples](https://www.plotline.so/blog/mobile-app-onboarding-examples) — 17 app breakdowns
- [Purchasely — App Onboarding](https://www.purchasely.com/blog/app-onboarding) — Paywall timing + health app patterns
- [UXCam — Top 10 Onboarding Flows](https://uxcam.com/blog/10-apps-with-great-user-onboarding/) — 2026 examples
- [Apple HIG — Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding) — Apple's official guidelines
- [VWO — Mobile App Onboarding Guide](https://vwo.com/blog/mobile-app-onboarding-guide/) — 2026 guide
