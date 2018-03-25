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
 - Forbidden hours for teachers {t, p}, {t, d}, {t, d, p}
 - Favourable hours for teachers {t, p}, {t, d}, {t, d, p}
 - Forbidden hours for groups {g, d, p}
 - Group overlap restriction {g1, g2}
 - Teacher overalap restriction {t1, t2}
 - Teacher overlap requirement {t1, t2}
 - No. of teaching days in a week {t, n_d}
 - Duration limit for groups {g, n_p}
 - Idle period constraints {t, k}
 - Lessons having fixed or forbidden  periods {t, s, g, n, [p], +/-}
 - Lessons having fixed or forbidden  periods {t, s, g, n, d, +/-}
 - Lessons that should / shouldn't be taught on consecutive days {t, s, g, n, +/-}
