# Authentication
TD Ameritrade requires an OAuth token. It is somewhat laborious to get this, but parts have been automated here with selenium. 


## Steps

### Step 1

Navigate and register/login to the [TD Developer page](https://developer.tdameritrade.com).

### Step 2
Navigate to My Apps

```eval_rst
.. image:: ./img/auth/1.png
    :scale: 100%
    :alt: auth1.png
```

### Step 3
Create a new one


### Step 4
Set the name and id to something reasonably unique, and the redirect to `http://localhost:8080` for now.


### Step 5
run `tdameritrade.auth.authentication` from a python prompt, with `client_id=consumer_key` and `redirect_uri` from step 4.

### Step 6
Sign in and authorize your app.

You can enter credentials by hand or store them in environment variables `TDAUSER` and `TDAPASS`. When stored, the first page will be filled in and advanced automaticly. 

```eval_rst
.. image:: ./img/auth/2.png
    :scale: 100%
    :alt: auth2.png

.. image:: ./img/auth/3.png
    :scale: 100%
    :alt: auth3.png
```

### Step 7
Return to the prompt, if you entered the info correctly you should see your tokens printed. Write these down, i recommend keeping a `keys.sh` file setting `ACCESS_TOKEN` and `REFRESH_TOKEN` environment variables. 


```eval_rst
.. image:: ./img/auth/4.png
    :scale: 100%
    :alt: auth4.png
```

