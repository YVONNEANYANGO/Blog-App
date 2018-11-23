<div class="navbar navbar-inverse" role="navigation">
    <div class="container-fluid">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">ADVENTURE</a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/home">HOME</a></li>
                <li><a href="/about">ABOUT</a></li>
                <li><a href="/latest">LATEST INFO</a></li>
                <li><a href="/contacts">CONTACTS</a></li>
            </ul>
        </div>
        
        <ul class="nav navbar-nav navbar-right">
            {% if current_user.is_authenticated %}
            <li style="color:cream;padding:15px;">{{current_user.username}}</li>
            <li><a href="{{url_for('auth.logout')}}">Sign out</a></li>
            {% else %}
            <li><a href="{{url_for('auth.login')}}">Sign in</a></li>
            {%endif%}
        </ul>
    </div>
</div>