#### 11.Container-With-Most-Water

| Step | left idx | right idx | height\[left] | height\[right] | width (right-left) | min height | area = width \* min height | max_area (so far) | Move pointer?                                     |
| ---- | -------- | --------- | ------------- | -------------- | ------------------ | ---------- | -------------------------- | ----------------- | ------------------------------------------------- |
| 1    | 0        | 8         | 1             | 7              | 8                  | 1          | 8 \* 1 = 8                 | 8                 | Move left (1 < 7)                                 |
| 2    | 1        | 8         | 8             | 7              | 7                  | 7          | 7 \* 7 = 49                | 49                | Move right (8 > 7)                                |
| 3    | 1        | 7         | 8             | 3              | 6                  | 3          | 6 \* 3 = 18                | 49                | Move right (8 > 3)                                |
| 4    | 1        | 6         | 8             | 8              | 5                  | 8          | 5 \* 8 = 40                | 49                | Move right (8 == 8, move either; here move right) |
| 5    | 1        | 5         | 8             | 4              | 4                  | 4          | 4 \* 4 = 16                | 49                | Move right (8 > 4)                                |
| 6    | 1        | 4         | 8             | 5              | 3                  | 5          | 3 \* 5 = 15                | 49                | Move right (8 > 5)                                |
| 7    | 1        | 3         | 8             | 2              | 2                  | 2          | 2 \* 2 = 4                 | 49                | Move right (8 > 2)                                |
| 8    | 1        | 2         | 8             | 6              | 1                  | 6          | 1 \* 6 = 6                 | 49                | Move right (8 > 6)                                |
| 9    | 1        | 1         | 8             | 8              | 0                  | 8          | 0 \* 8 = 0                 | 49                | End (left == right)                               |
