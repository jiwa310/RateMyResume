/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
}

module.exports = {
  async rewrites() {
    return [
      {
        source: '/fastapi/:path*',
        destination: 'http://localhost:8000/:path*', // Proxy to FastAPI
      },
    ]
  },
}

