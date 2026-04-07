import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

// Routes that don't require authentication
const PUBLIC_ROUTES = ["/login", "/api/auth/login"];

// Role hierarchy for access control (kept for future use)
const ROLE_HIERARCHY: Record<string, number> = {
  Admin: 3,
  Analyst: 2,
  Reviewer: 1,
};

// Route access requirements (kept for future use)
const PROTECTED_ROUTES: Record<string, string> = {
  "/users": "Admin",
  "/settings": "Admin",
  "/audit-logs": "Analyst",
};

export function middleware(request: NextRequest) {
  try {
    const { pathname } = request.nextUrl;

    // Allow public routes
    if (PUBLIC_ROUTES.some((route) => pathname.startsWith(route))) {
      return NextResponse.next();
    }

    // Allow API routes except protected ones
    if (
      pathname.startsWith("/api/") &&
      !pathname.startsWith("/api/auth/users")
    ) {
      return NextResponse.next();
    }

    // 🔥 IMPORTANT: No server-side auth enforcement for now
    // Auth is handled client-side using JWT
    return NextResponse.next();
  } catch (err) {
    console.error("Middleware crashed:", err);

    // 🔥 NEVER break request
    return NextResponse.next();
  }
}

export const config = {
  matcher: [
    "/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)",
  ],
};
