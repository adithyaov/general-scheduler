# UI
---
### Correctness
 - no of periods
 - no of week days
 - instructors
 - coursenames
 - groups
 - rooms
 - course
 -- instructor
 -- coursename
 -- groups
 -- lessons in week with duration(1)
 -- room constraints

### Comfort
 1. Forbidden hours for teachers {t, p}, {t, d}, {t, d, p}
 2. Favourable hours for teachers {t, p}, {t, d}, {t, d, p}
 3. Forbidden hours for groups {g, d, p}
 4. Group overlap restriction {g1, g2}
 5. Teacher overalap restriction {t1, t2}
 6. Teacher overlap requirement {t1, t2}
 7. No. of teaching days in a week {t, n_d}
 8. Duration limit for groups {g, n_p}
 9. Idle period constraints {t, k}
 10. Lessons having fixed or forbidden  periods {t, s, g, n, [p], +/-}
 11. Lessons having fixed or forbidden  periods {t, s, g, n, d, +/-}
 12. Lessons that should / shouldn't be taught on consecutive days {t, s, g, n, +/-}
