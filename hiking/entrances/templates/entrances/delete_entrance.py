{% extends "layout.html" %}
{% block content %}
<div class="jumbotron">
  <h1>Would you like to remove the hike?</h1>
  <p>Fill out the form to remove the entrance from the list.</p>
  <form method="POST">
      {# This hidden_tag is a CSRF security feature. #}
      {{ form.hidden_tag() }}
      {{ form.id.label }} {{ form.id() }}
      {{ form.submit() }}
  </form>
</div>
{% endblock %}
