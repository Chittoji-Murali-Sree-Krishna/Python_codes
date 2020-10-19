# rendering css and js and images
## css
```html
<link rel="stylesheet" href="{{url_for('static', filename='css/main.css')}}">
```

## javaScript
```html
<script src="{{url_for('static', filename='js/script.js')}}"></script>
```


## images
```html
<img src="{{url_for('static', filename='images/mypic.jpg')}}" alt="" class="intro__img" />
```
