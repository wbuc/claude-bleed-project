# Add Apple Smart App Banner to Next.js landing page

Add a Smart App Banner so iPhone users see a native iOS banner at the top of the page prompting them to open or download the Bleed app from the App Store.

## Setup

### 1. Add the environment variable

In your `.env.local` (or `.env`):

```
NEXT_PUBLIC_APP_STORE_ID=123456789
```

Replace `123456789` with the actual App Store ID found in App Store Connect under App Information > General > Apple ID.

### 2. Add the meta tag

In `app/layout.tsx` (App Router) or `pages/_app.tsx` (Pages Router), add the meta tag inside the `<head>`.

**App Router (`app/layout.tsx`):**

```tsx
export const metadata = {
  other: {
    'apple-itunes-app': `app-id=${process.env.NEXT_PUBLIC_APP_STORE_ID}`,
  },
};
```

**Pages Router (`pages/_document.tsx`):**

```tsx
<Head>
  <meta
    name="apple-itunes-app"
    content={`app-id=${process.env.NEXT_PUBLIC_APP_STORE_ID}`}
  />
</Head>
```

Do not hardcode the app ID. It must come from the environment variable.

### 3. Optional: pass page context to the app

If you want the app to open to a specific screen based on the page the user is on:

```tsx
'apple-itunes-app': `app-id=${process.env.NEXT_PUBLIC_APP_STORE_ID}, app-argument=${pageUrl}`,
```

This lets you parse the URL in the app and route the user to the right place.

## What the banner does (no custom code needed)

- App installed: shows "Open" and opens the app
- App not installed: shows "View" and links to the App Store
- Device doesn't support the app or unavailable in that region: banner doesn't appear
- User dismisses it: won't reappear on that page

## Source

[Apple Developer - Promoting Apps with Smart App Banners](https://developer.apple.com/documentation/webkit/promoting-apps-with-smart-app-banners)
