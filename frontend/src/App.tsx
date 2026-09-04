import { useEffect, useState } from 'react'

function App() {
  const [backendStatus, setBackendStatus] = useState<'Connected' | 'Offline'>('Offline')

  useEffect(() => {
    const controller = new AbortController()

    fetch('http://localhost:8000/', { signal: controller.signal })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Backend health check failed')
        }

        setBackendStatus('Connected')
      })
      .catch((error: unknown) => {
        if (error instanceof DOMException && error.name === 'AbortError') {
          return
        }

        setBackendStatus('Offline')
      })

    return () => controller.abort()
  }, [])

  return (
    <main className="relative flex min-h-screen items-center justify-center overflow-hidden bg-[#fffdfb] px-6 py-12 text-[#514b61]">
      <div className="pointer-events-none absolute -left-24 top-[-5rem] h-72 w-72 rounded-full bg-[#e7defb] opacity-80 blur-3xl" />
      <div className="pointer-events-none absolute -right-20 bottom-[-6rem] h-80 w-80 rounded-full bg-[#f8dce5] opacity-75 blur-3xl" />
      <div className="pointer-events-none absolute bottom-1/4 left-1/4 h-40 w-40 rounded-full bg-[#d9f3e7] opacity-60 blur-3xl" />

      <div
        className={`absolute right-6 top-6 inline-flex items-center gap-2 rounded-full border px-3 py-2 text-xs font-semibold tracking-wide shadow-sm backdrop-blur-sm sm:right-8 sm:top-8 ${
          backendStatus === 'Connected'
            ? 'border-[#c8e8d8] bg-[#effaf4] text-[#5e9275]'
            : 'border-[#eadfe5] bg-white/80 text-[#9a8792]'
        }`}
      >
        <span
          className={`h-2 w-2 rounded-full ${
            backendStatus === 'Connected'
              ? 'animate-pulse bg-[#82c89f]'
              : 'bg-[#cbbbc5]'
          }`}
        />
        {backendStatus}
      </div>

      <section className="relative flex w-full max-w-2xl flex-col items-center rounded-[2rem] border border-white/90 bg-white/70 px-8 py-20 text-center shadow-[0_24px_80px_rgba(104,88,132,0.12)] backdrop-blur-sm sm:px-16">
        <span className="mb-7 inline-flex items-center gap-2 rounded-full border border-[#e5dbf7] bg-[#f7f2ff] px-4 py-2 text-xs font-semibold uppercase tracking-[0.22em] text-[#8877a5]">
          <span className="h-2 w-2 rounded-full bg-[#9ed8c0]" />
          Thoughtful trading
        </span>
        <h1 className="max-w-lg text-5xl font-semibold tracking-[-0.04em] text-[#514562] sm:text-7xl">
          Chronos Trade
        </h1>
        <p className="mt-6 max-w-md text-base leading-7 text-[#81788c] sm:text-lg">
          A calm space for making better moves, one moment at a time.
        </p>
        <div className="mt-10 flex items-center gap-3" aria-hidden="true">
          <span className="h-1.5 w-10 rounded-full bg-[#d9c9f3]" />
          <span className="h-1.5 w-16 rounded-full bg-[#c4ead7]" />
          <span className="h-1.5 w-6 rounded-full bg-[#f1c5d3]" />
        </div>
      </section>
    </main>
  )
}

export default App
