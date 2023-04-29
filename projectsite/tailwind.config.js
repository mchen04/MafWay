/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        ncc: {
          beige: "#EFE8DF",
          black: "#0F0A0A",
          grey: "#6D6875",
          white: "#F7F7FF",
          brown: "#1E140B",
          green: "#3B6662",
      backgroundImage: {
        'field': "url('/public/field.jpeg')",
      },
    },
  },
},
  plugins: [],
}
}
