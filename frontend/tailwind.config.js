/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html",
  "./src/**/*.{js,ts,jsx,tsx,vue}"],
  theme: {
    extend: {
      keyframes: {
        fadeInOut: {
          '0%': {
            opacity: '0',
          },
          '50%': {
            opacity: '1',
          },
          '100%': {
            opacity: '0',
          },
      },
    },
    animation:{
      fade: 'fadeInOut 5s  linear ' 
    },
  },
  plugins: [],
}
}
