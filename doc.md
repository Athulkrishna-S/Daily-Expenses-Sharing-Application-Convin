



# Covin





# userAPIs

### POST Create User

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
|body|body|object| yes |none|
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



### GET getUserDetails

endpoint : /user/getDetail

> Body Parameters



### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| yes |none|
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



# ExpenseAPIs

### POST addExpense

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
|Authorization|header|string| yes |none|
|body|body|object| yes |none|

> Response Examples

> 200 Response

```json
{
  "message": "string",
  "statusCode": 0
}
```


### GET DownloadBalanceSheet

endpoint : /expense/download/balanacesheet

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| yes |none|



### GET Retrieve individual user expenses.

endpoint : /expense/userexp





### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| yes |none|


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



### GET Retrieve overall expenses.

endpoint : /expense/fullexp

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| no |none|

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



# AuthAPIs

### POST Login

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
|body|body|object| yes |none|

> Response Examples

> 200 Response

```json
{
  "statusCode": 0,
  "token": "string"
}
```



### GET Logout

endpoint : /user/logout

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| yes |none|

> Response Examples

> 200 Response

```json
{
  "msg": "string"
}
```





