/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
}

module.exports = {
  async rewrites() {
    return [
      {
        source: '/fastapi/:path*',
        destination: 'https://fastapi-git-jim-jims-projects-90f7dc86.vercel.app/:path*', // Proxy to FastAPI
      },
    ]
  },
}

