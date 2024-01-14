/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
}

module.exports = {
  async rewrites() {
    return [
      {
        source: '/fastapi/:path*',
        destination: 'https://fastapi-green.vercel.app/:path*', // Proxy to FastAPI
      },
    ]
  },
}

