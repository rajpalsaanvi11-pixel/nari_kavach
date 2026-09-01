---
name: VeilAI
colors:
  surface: '#fef8f3'
  surface-dim: '#ded9d4'
  surface-bright: '#fef8f3'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f8f3ee'
  surface-container: '#f3ede8'
  surface-container-high: '#ede7e2'
  surface-container-highest: '#e7e1dd'
  on-surface: '#1d1b19'
  on-surface-variant: '#514346'
  inverse-surface: '#32302d'
  inverse-on-surface: '#f6f0eb'
  outline: '#837376'
  outline-variant: '#d5c2c5'
  surface-tint: '#874d5f'
  primary: '#874d5f'
  on-primary: '#ffffff'
  primary-container: '#e8a0b4'
  on-primary-container: '#6b3546'
  inverse-primary: '#fcb2c6'
  secondary: '#655781'
  on-secondary: '#ffffff'
  secondary-container: '#deccfd'
  on-secondary-container: '#62547e'
  tertiary: '#7e506e'
  on-tertiary: '#ffffff'
  tertiary-container: '#dca4c6'
  on-tertiary-container: '#633854'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffd9e1'
  primary-fixed-dim: '#fcb2c6'
  on-primary-fixed: '#370b1c'
  on-primary-fixed-variant: '#6c3647'
  secondary-fixed: '#eaddff'
  secondary-fixed-dim: '#d0bfef'
  on-secondary-fixed: '#21143a'
  on-secondary-fixed-variant: '#4d4068'
  tertiary-fixed: '#ffd8ed'
  tertiary-fixed-dim: '#efb6d8'
  on-tertiary-fixed: '#320d28'
  on-tertiary-fixed-variant: '#643955'
  background: '#fef8f3'
  on-background: '#1d1b19'
  surface-variant: '#e7e1dd'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Nunito Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Nunito Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Nunito Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  caption:
    fontFamily: Nunito Sans
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 120px
---

## Brand & Style

The design system is centered on a "Protective Sanctuary" aesthetic—a blend of modern minimalism and soft tactile elements. It aims to evoke a sense of safety, empowerment, and digital privacy without the cold, clinical feel of traditional security software. The UI utilizes a "Soft-Modern" approach, characterized by organic shapes, generous breathing room, and a gentle color palette that feels approachable for women and teens.

The emotional response should be one of calm control. By avoiding aggressive "alert" visuals and instead using soft blurs and rounded geometry, the interface transforms privacy management from a chore into a self-care ritual.

## Colors

The palette uses a warm off-white base to reduce eye strain and create a "paper-like" tactility. 

- **Primary (Dusty Rose):** Used for primary actions, active states, and brand-building elements.
- **Secondary (Soft Lavender):** Used for progressive disclosure, secondary features, and subtle highlights.
- **Accent (Deep Plum):** Reserved for high-priority Call-to-Actions (CTAs) and text emphasis to ensure legibility and visual hierarchy.
- **Functional Colors:** Sage green and warm coral are muted to maintain the soft aesthetic while providing clear status feedback.

Color application should favor large areas of neutral background with intentional, soft pops of the primary and secondary hues.

## Typography

This design system uses a pairing of **Plus Jakarta Sans** for headlines to provide a friendly, optimistic, and modern character, and **Nunito Sans** for body text to ensure maximum readability with a gentle, rounded touch.

- **Scale:** Headlines should have ample margin-bottom to establish clear section breaks.
- **Readability:** Body text never drops below 16px to maintain accessibility for all users.
- **Weight:** Use SemiBold (600) for interactive labels and Bold (700) sparingly for high-level display text.

## Layout & Spacing

The layout follows a **Fluid Grid** model with high-containment margins to create a focused "reading lane" in the center of the screen.

- **Desktop:** 12-column grid with a max-width of 1280px. Use wide outer margins to center the content and evoke a sense of calm.
- **Mobile:** Single-column layout with 20px side margins. Elements should be full-width "cards" to maximize the hit area for touch.
- **Rhythm:** Use the 8px base unit for all spatial relationships. Section breaks should be aggressive (80px+) to prevent information density from feeling overwhelming.

## Elevation & Depth

Elevation is communicated through **Ambient Shadows** and **Tonal Layers** rather than harsh borders.

- **Surface Levels:** The base layer is the Neutral Cream. Primary content containers (Cards) use a pure White (#FFFFFF) to pop subtly against the background.
- **Shadows:** Use extremely diffused shadows with a slight Deep Plum (#6B3F5C) tint at very low opacity (5-8%). This creates a "floating" effect that feels light and airy.
- **Transitions:** Use soft blurs (Backdrop Filter: 12px) for overlays and navigation bars to maintain a sense of context and depth.

## Shapes

The shape language is inherently "Soft." Sharp corners are avoided to maintain the protective and welcoming tone.

- **Standard Elements:** Buttons, input fields, and small cards use a 0.5rem (8px) radius.
- **Feature Containers:** Large cards or "Sanctuary" areas use a 1.5rem (24px) radius to feel more organic and enclosed.
- **Icons:** Icons should be simple line-style with rounded caps and joins, matching the stroke weight of the typography.

## Components

- **Buttons:** Primary buttons use the Deep Plum background with White text for high contrast. Secondary buttons use the Dusty Rose background with Plum text. All buttons have a minimum height of 48px for accessibility.
- **Input Fields:** Fields are styled with a subtle 1px border in a muted Lavender and a soft White fill. On focus, the border transitions to Primary Dusty Rose with a soft outer glow.
- **Cards:** Cards are the primary organizational unit. They should feature a White background, the "rounded-xl" radius, and a soft ambient shadow.
- **Chips/Badges:** Used for privacy status (e.g., "Protected"). These should be pill-shaped with low-saturation background colors (Sage or Lavender) and dark text.
- **Privacy Toggle:** A custom-styled switch that is larger than standard system toggles, using the Dusty Rose for the "On" state to feel rewarding and positive.
- **Progress Indicators:** Use soft, rounded bars. Avoid "loading spinners" where possible, opting for shimmering skeleton states to maintain a calm UI flow.