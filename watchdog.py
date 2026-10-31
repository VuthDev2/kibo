"""Simulate battery monitoring while navigating ten waypoints."""

import random


battery = 100.0

for waypoint in range(1, 11):
    battery -= random.uniform(1.5, 3.5)
    print(f"[NAV] Waypoint {waypoint}/10 reached. Battery: {battery:.2f}%")

    if battery < 75:
        print("[EMERGENCY RETURN TRIGGERED]")
        break
    elif battery < 80:
        print("[CAUTION] Battery below 80%")
else:
    print("[DONE] All waypoints completed.")
