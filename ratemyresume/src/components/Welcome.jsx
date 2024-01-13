import React from 'react';

// Define your WelcomePage component
export default function WelcomePage() {
  return (
    <div className="min-h-screen text-center pt-10 md:pt-5 pl-10 md:pl-20 pr-10 md:pr-20">
        <h1 className="text-red-300 text-xl md:text-5xl font-bold mb-4">Get Feedback ASAP</h1>
        <div className="flex flex-col items-center justify-center border-2 border-dashed border-red-300 p-10 mt-8 rounded-md">
            <label htmlFor="file-upload" className="flex flex-col items-center px-2 py-1 bg-red-300 text-red-900 rounded-lg shadow-lg tracking-wide uppercase border border-blue cursor-pointer hover:bg-red-400 hover:text-red-900">
                <svg className="w-6 h-6" fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M16 7a4 4 0 00-4-4H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V9a2 2 0 00-2-2zm-4-2a2 2 0 012 2v1a2 2 0 01-2 2h-2a2 2 0 01-2-2V5a2 2 0 012-2h2zm-1 8l3 3m0-3l-3 3m3-3H5"></path></svg>
                <span className="mt-2 text-base leading-normal">Upload resume</span>
                <input type='file' className="hidden" id="file-upload" accept=".pdf"/>
            </label>
            <p className="mt-2 text-gray-300">or drag resume here</p>
        </div>
    </div>
  );
}
