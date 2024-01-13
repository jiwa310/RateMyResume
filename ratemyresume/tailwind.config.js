/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    height: {
      '15': '3.75rem'
    },
    extend: {
      fontFamily: {
        'league-spartan': ['var(--font-league-spartan)', 'sans-serif'],
      },
      fontSize: {
        'name': '4rem', // Very large for your name on the front page
        'section-title': '2rem', // Large for section titles
        'entry-title': '1.5rem', // A little smaller for experience/project titles
      },
      fontWeight: {
        'name': '700', // Bold for your name on the front page
        'section-title': '600', // Not as bold for section titles
      },
      boxShadow: {
        yellow: '0 10px 15px -3px rgba(252, 211, 77, 0.4), 0 4px 6px -2px rgba(252, 211, 77, 0.1)',
      },
    },
  },
  variants: {
    extend: {
      opacity: ['responsive', 'hover', 'focus', 'group-hover', 'delay-2000'],
    },
  },
  plugins: [],
}
