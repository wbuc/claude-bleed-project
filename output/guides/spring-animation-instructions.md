# Spring Animation Instructions for Sheets

Paste the block below into your LLM when working on your SwiftUI app.

All values are sourced from Apple's documentation and verified SwiftUI guides (sources at the bottom).

---

## Prompt to paste:

```
RULE: Every animation in this app MUST use spring curves. Never use .linear or .easeInOut
for user-initiated actions. This applies to sheets, modals, transitions, button states,
and any element that moves in response to user input.

EXCEPTION: Loading spinners, progress bars, and auto-playing loops may use .linear or
.easeInOut since they are system-driven, not user-driven.
(Source: createwithswift.com — springs are recommended for user-triggered interactions,
not for automatic animations like loading spinners)


## Spring API to Use

If targeting iOS 17+, prefer the modern preset API:
- .smooth              → No bounce, elegant (default duration: 0.5, bounce: 0.0)
- .snappy              → Small bounce, brisk (default duration: 0.5)
- .bouncy              → Medium bounce, playful (default duration: 0.5)

These are customizable:
- .smooth(duration: 0.35)
- .snappy(duration: 0.25)
- .bouncy(duration: 0.4, extraBounce: 0.1)

If targeting iOS 16 or needing fine control, use the explicit spring:
- .spring(response:dampingFraction:blendDuration:)

Apple's default values for .spring() are:
  response: 0.5, dampingFraction: 0.825, blendDuration: 0
(Source: Apple Developer Documentation — spring(response:dampingFraction:blendDuration:))

For interactive/gesture-driven animations, use:
  .interactiveSpring(response: 0.15, dampingFraction: 0.86, blendDuration: 0.25)
(Source: Apple Developer Documentation — interactiveSpring)


## Parameter Guide

response = speed. Lower = faster animation.
  - 0.3 = quick and snappy, ideal for small UI feedback like button presses
  - 0.55 = default, balanced
  - 0.9 = slower, more deliberate, for modal presentations
  (Source: createwithswift.com)

dampingFraction = bounciness. Lower = more bounce.
  - 0.5 = more bounce
  - 0.75 = balanced default
  - 0.95 = subtle, almost no bounce
  (Source: createwithswift.com, GetStream/swiftui-spring-animations)

bounce (iOS 17+ API) = springiness.
  - 0.0 = no bounce (smooth)
  - 0.15 = brisk, not bouncy
  - 0.3 = larger overshoot, playful
  - 0.6 = highly playful, exaggerated
  (Source: GetStream/swiftui-spring-animations)


## Bleed App Decision: Native Sheets + Spring Content

We use Apple's native .sheet() for all sheet presentations. The sheet slide-up animation
is handled by iOS — we do NOT override it with custom overlays.

The premium feel comes from spring-animating the CONTENT inside the sheet after it lands.
This follows Apple's own pattern and avoids over-engineering animations.

Reasoning:
- Native .sheet() gives users the familiar iOS feel they expect
- Swipe-to-dismiss, keyboard avoidance, and accessibility come free
- Custom sheet overlays add complexity without meaningful UX improvement
- Restraint > overkill — premium apps feel polished, not bouncy everywhere


## 1. Sheet Content Animation (Primary Pattern — Use This)

Use native .sheet() for presentation. Spring-animate the content inside on appear.
The sheet slides up with Apple's animation, then content settles in with a spring.

struct TermsView: View {
    @State private var appeared = false

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                // Your content
            }
            .padding()
        }
        .scaleEffect(appeared ? 1 : 0.92)
        .opacity(appeared ? 1 : 0)
        .offset(y: appeared ? 0 : 20)
        .onAppear {
            withAnimation(.bouncy(duration: 0.5, extraBounce: 0.08)) {
                appeared = true
            }
        }
    }
}

Apply this pattern to ALL sheet content views:
- Terms of Service, Privacy Policy
- Settings, logging sheets, detail views
- Any view presented via .sheet() or .fullScreenCover()

The three properties that animate together:
- scaleEffect: 0.92 → 1.0 (subtle grow-in)
- opacity: 0 → 1 (fade in)
- offset y: 20 → 0 (slight upward settle)

Trigger: single withAnimation(.bouncy) block on .onAppear
(Source: Apple Documentation — .bouncy preset, iOS 17+)


## 2. Custom Half-Sheet (Reference Only — Not Used in Bleed)

If you ever need full control over the sheet animation itself (not just content),
here is a custom spring-animated overlay. Bleed does NOT use this — we use native
.sheet() instead. Kept here for reference only.

struct SpringSheet<Content: View>: View {
    @Binding var isPresented: Bool
    @ViewBuilder let content: () -> Content

    @State private var dragOffset: CGFloat = 0

    private let sheetHeight: CGFloat = UIScreen.main.bounds.height * 0.45

    var body: some View {
        ZStack(alignment: .bottom) {
            if isPresented {
                Color.black
                    .opacity(0.3 * (1 - dragOffset / sheetHeight))
                    .ignoresSafeArea()
                    .onTapGesture { isPresented = false }
                    .transition(.opacity)
            }

            if isPresented {
                VStack(spacing: 0) {
                    Capsule()
                        .fill(Color(.systemGray4))
                        .frame(width: 36, height: 5)
                        .padding(.top, 8)
                        .padding(.bottom, 12)

                    content()
                }
                .frame(maxWidth: .infinity)
                .frame(height: sheetHeight)
                .background(
                    RoundedRectangle(cornerRadius: 24, style: .continuous)
                        .fill(.regularMaterial)
                )
                .offset(y: max(dragOffset, 0))
                .gesture(
                    DragGesture()
                        .onChanged { value in
                            dragOffset = value.translation.height
                        }
                        .onEnded { value in
                            if value.translation.height > sheetHeight * 0.4 ||
                               value.predictedEndTranslation.height > sheetHeight * 0.5 {
                                isPresented = false
                            }
                            dragOffset = 0
                        }
                )
                .transition(.move(edge: .bottom))
            }
        }
        .animation(.snappy(duration: 0.35), value: isPresented)
        .animation(.interactiveSpring(response: 0.15, dampingFraction: 0.86), value: dragOffset)
    }
}


## 3. Full-Screen Cover with Spring

Animate elements inside with staggered springs:

struct DetailView: View {
    @State private var appeared = false
    @Environment(\.dismiss) var dismiss

    var body: some View {
        VStack(spacing: 20) {
            headerSection
                .offset(y: appeared ? 0 : -20)
            contentSection
                .offset(y: appeared ? 0 : 30)
            actionButtons
                .offset(y: appeared ? 0 : 50)
        }
        .opacity(appeared ? 1 : 0)
        .onAppear {
            withAnimation(.snappy(duration: 0.4)) {
                appeared = true
            }
        }
    }
}


## 4. Button Press States (Apply to ALL Buttons)

struct SpringPressStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .scaleEffect(configuration.isPressed ? 0.95 : 1.0)
            .opacity(configuration.isPressed ? 0.85 : 1.0)
            .animation(.snappy(duration: 0.25), value: configuration.isPressed)
            // iOS 16 alternative:
            // .animation(.spring(response: 0.3, dampingFraction: 0.75), value: configuration.isPressed)
    }
}

Apply globally or per button:
    Button("Log Period") { }
        .buttonStyle(SpringPressStyle())

Response of 0.3 is "quick and snappy, ideal for small UI feedback like button presses"
(Source: createwithswift.com)


## 5. Spring Values Reference

### iOS 17+ (preferred — use presets)

| Context              | Preset                                       | Notes                                     |
|----------------------|----------------------------------------------|-------------------------------------------|
| Sheet presentation   | Native .sheet() (Apple default)              | Do NOT override — let iOS handle it       |
| Sheet content appear | .bouncy(duration: 0.5, extraBounce: 0.08)    | Scale 0.92→1 + fade + offset inside sheet |
| Button press         | .snappy(duration: 0.25)                      | Fast, clean, modern iOS feel              |
| Content appear       | .smooth(duration: 0.35)                      | Soft entrance, no bounce                  |
| Tab switch           | .snappy(duration: 0.25)                      | Fast, minimal bounce                      |
| Card expand          | .bouncy(duration: 0.4)                       | Satisfying overshoot                      |
| Playful/celebration  | .bouncy(extraBounce: 0.1)                    | Extra springiness for delight moments     |
| Dismiss (flick)      | .snappy(duration: 0.25)                      | Fast exit                                 |

.snappy = "fast, clean, feels like modern iOS"
.smooth = soft UI transitions
.bouncy = lively UI with personality
(Source: dev.to/sebastienlato — SwiftUI Animation Masterclass)

### iOS 16 (explicit spring)

| Context              | response | dampingFraction | Source                          |
|----------------------|----------|-----------------|---------------------------------|
| General purpose      | 0.32     | 0.72            | dev.to SwiftUI Masterclass      |
| Card expansion       | 0.28     | 0.78            | dev.to SwiftUI Masterclass      |
| Interactive gestures | 0.30     | 0.80            | dev.to SwiftUI Masterclass      |
| Expanding card       | 0.30     | 0.82            | dev.to SwiftUI Masterclass      |
| Apple default        | 0.50     | 0.825           | Apple Documentation             |
| Interactive default  | 0.15     | 0.86            | Apple Documentation             |
| Custom toggle        | 0.35     | (balanced)      | createwithswift.com             |

### What NOT to use for user-initiated actions:
- .linear (robotic, no life)
- .easeInOut (generic, no spring feel)
- .easeIn or .easeOut alone
- .animation(.default) without specifying spring


## 6. Pair Springs with Haptics

Every spring animation on a user-initiated action should pair with haptic feedback:

Button(action: {
    UIImpactFeedbackGenerator(style: .light).impactOccurred()
    // action
}) {
    Text("Save")
}
.buttonStyle(SpringPressStyle())

For sheets opening:
    UIImpactFeedbackGenerator(style: .medium).impactOccurred()
    withAnimation(.snappy(duration: 0.35)) {
        showSheet = true
    }

For sheet dismiss via drag:
    UIImpactFeedbackGenerator(style: .light).impactOccurred()
    isPresented = false

Apps with haptics see 18% boost in perceived quality and 8% more engagement.
(Source: HackerNoon — iOS Guide to Haptic Feedback)


## 7. Replacing Existing Animations

Search the codebase for these patterns and replace:

FIND                                    → REPLACE WITH (iOS 17+)
.animation(.default)                    → .animation(.snappy)
.animation(.easeInOut)                  → .animation(.snappy)
.animation(.easeIn(duration: X))        → .animation(.smooth(duration: X))
.animation(.linear)                     → .animation(.smooth) [only for user actions]
withAnimation { }                       → withAnimation(.snappy) { }
withAnimation(.easeInOut) { }           → withAnimation(.snappy) { }

FIND                                    → REPLACE WITH (iOS 16)
.animation(.default)                    → .animation(.spring(response: 0.5, dampingFraction: 0.825))
.animation(.easeInOut)                  → .animation(.spring(response: 0.5, dampingFraction: 0.825))
withAnimation { }                       → withAnimation(.spring(response: 0.5, dampingFraction: 0.825)) { }
```

---

## How to Use This

1. Copy everything between the triple backticks above
2. Paste it into your LLM as a system instruction or at the start of a conversation
3. Tell it: "Apply these spring animation rules to all sheets in my app"
4. For new sheets: "Build a logging sheet for [feature] using the SpringSheet pattern"

---

## Sources

All values in this file are sourced from:

- **Apple Documentation** — [spring(response:dampingFraction:blendDuration:)](https://developer.apple.com/documentation/SwiftUI/Animation/spring(response:dampingFraction:blendDuration:)) — default values: response 0.5, dampingFraction 0.825
- **Apple Documentation** — [interactiveSpring](https://developer.apple.com/documentation/swiftui/animation/interactivespring(response:dampingfraction:blendduration:)) — default values: response 0.15, dampingFraction 0.86
- **Apple Documentation** — [.smooth](https://developer.apple.com/documentation/SwiftUI/Animation/smooth), [.snappy](https://developer.apple.com/documentation/SwiftUI/Animation/snappy), [.bouncy](https://developer.apple.com/documentation/SwiftUI/Animation/bouncy) — iOS 17+ presets
- **createwithswift.com** — [Understanding Spring Animations in SwiftUI](https://www.createwithswift.com/understanding-spring-animations-in-swiftui/) — response/dampingFraction ranges, use cases, interactiveSpring recommendation
- **GetStream/swiftui-spring-animations** — [GitHub reference repo](https://github.com/GetStream/swiftui-spring-animations) — bounce parameter values, preset explanations
- **Hacking with Swift** — [How to create a spring animation](https://www.hackingwithswift.com/quick-start/swiftui/how-to-create-a-spring-animation) — Paul Hudson's recommendations, iOS 17+ API preference
- **dev.to/sebastienlato** — [SwiftUI Animation Masterclass](https://dev.to/sebastienlato/swiftui-animation-masterclass-springs-curves-smooth-motion-3e4o) — real-world spring values for cards, gestures, general purpose
- **HackerNoon** — [iOS Guide to Haptic Feedback](https://hackernoon.com/the-ios-guide-to-haptic-feedback) — haptic pairing stats (18% quality boost, 8% engagement)
