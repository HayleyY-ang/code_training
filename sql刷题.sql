------------行转列，行转列---------------------
-- 使用数据透视表
SELECT *
FROM student
PIVOT (
    SUM(score) FOR subject IN (语文, 数学, 英语)
)

--case when
SELECT name,

  MAX(CASE WHEN subject='语文' THEN score ELSE 0  END) AS "语文",
  MAX(
  CASE
    WHEN subject='数学'
    THEN score
    ELSE 0
  END) AS "数学",
  MAX(
  CASE
    WHEN subject='英语'
    THEN score
    ELSE 0
  END) AS "英语"
FROM student
GROUP BY name

------- 行转列

select * from student1 unpivot(score for subject in ('语文','数学','英语'))

SELECT
    NAME,
    '语文' AS subject ,
    MAX("语文") AS score
FROM student1 GROUP BY NAME
UNION
SELECT
    NAME,
    '数学' AS subject ,
    MAX("数学") AS score
FROM student1 GROUP BY NAME
UNION
SELECT
    NAME,
    '英语' AS subject ,
    MAX("英语") AS score
FROM student1 GROUP BY NAME

