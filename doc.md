---
title: Covin
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.23"

---

# Covin



# Authentication

# userAPIs

## POST Create User

endpoint : /user/create

> Body Parameters

```json
{
  "name": "Rohit",
  "mobile": 9559559556,
  "email": "cc@gmail.com"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» name|body|string| yes |none|
|» mobile|body|integer| yes |none|
|» email|body|string| yes |none|

> Response Examples

> 201 Response

```json
{
  "message": "string",
  "statusCode": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|Inline|

### Responses Data Schema

HTTP Status Code **201**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» statusCode|integer|true|none||none|

## GET getUserDetails

endpoint : /user/getDetail

> Body Parameters

```json
{
  "email": "aa@gmail.com"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| no |none|
|body|body|object| no |none|

> Response Examples

> 200 Response

```json
{
  "email": "string",
  "expenses": {},
  "mobile": 0,
  "name": "string",
  "statusCode": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» email|string|true|none||none|
|» expenses|object|true|none||none|
|» mobile|integer|true|none||none|
|» name|string|true|none||none|
|» statusCode|integer|true|none||none|

# ExpenseAPIs

## POST addExpense

endpoint : /expense/add

> Body Parameters

```json
{
  "payer": "cc@gmail.com",
  "amount": 600,
  "participants": {
    "bb@gmail.com": 200,
    "aa@gmail.com": 50,
    "cc@gmail.com": 350
  },
  "method": "exact",
  "purpose": "Munnar Trip"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| no |none|
|body|body|object| no |none|

> Response Examples

> 200 Response

```json
{
  "message": "string",
  "statusCode": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» statusCode|integer|true|none||none|

## GET DownloadBalanceSheet

endpoint : /expense/download/balanacesheet

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| no |none|

> Response Examples

> 200 Response

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

## GET Retrieve individual user expenses.

endpoint : /expense/userexp

> Body Parameters

```json
{
  "email": "aa@gmail.com"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| no |none|
|body|body|object| no |none|

> Response Examples

> 200 Response

```json
{
  "Expenses": {
    "Dinner at Olive Garden": 0,
    "Lunch": 0
  },
  "StatusCode": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» Expenses|object|true|none||none|
|»» Dinner at Olive Garden|integer|true|none||none|
|»» Lunch|integer|true|none||none|
|» StatusCode|integer|true|none||none|

## GET Retrieve overall expenses.

endpoint : /expense/fullexp

> Response Examples

> 200 Response

```json
{
  "Data": {
    "Dinner at Olive Garden": 0,
    "Lunch": 0,
    "Total": 0
  },
  "StatusCode": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» Data|object|true|none||none|
|»» Dinner at Olive Garden|integer|true|none||none|
|»» Lunch|integer|true|none||none|
|»» Total|integer|true|none||none|
|» StatusCode|integer|true|none||none|

# AuthAPIs

## POST Login

endpoint : /user/login

> Body Parameters

```json
{
  "name": "Rohit",
  "mobile": 9559559556,
  "email": "cc@gmail.com"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|

> Response Examples

> 200 Response

```json
{
  "statusCode": 0,
  "token": "string"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» statusCode|integer|true|none||none|
|» token|string|true|none||none|

## GET Logout

endpoint : /user/logout

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| no |none|

> Response Examples

> 200 Response

```json
{
  "msg": "string"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» msg|string|true|none||none|

# Data Schema

