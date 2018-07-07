<!DOCTYPE html>
<html lang="en">
	<head>
		<title>TexT SummarizeR.</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<!--<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
		<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
	-->
		<!-- Latest compiled and minified CSS -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

		<!-- jQuery library -->
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

		<!-- Latest compiled JavaScript -->
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
		<!-- Custom styles for this template -->
		<link href="navbar.css" rel="stylesheet">
	</head>
	
	<body background="C:\Users\NI40006105\Desktop\project\pics\pic1.jpg">
		 <div class="navbar-wrapper">
		  <div class="container">

			<nav class="navbar navbar-inverse navbar-static-top">
			  <div class="container">
				<div class="navbar-header">
				  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				  </button>
				  <a class="navbar-brand" style="text-align:center" href="#">TexT SummarizeR.</a>
				</div>
				<div id="navbar" class="navbar-collapse collapse">
				  <ul class="nav navbar-nav" style="float:right">
					<li class="active" ><a href="#">Home</a></li>
					<li><a href="#about">About</a></li>
					<li><a href="#kinds">Kinds</a></li>
				  </ul>
				</div>
			  </div>
			</nav>

			<div>
			  <a href="#" id="start_button" onclick="startDictation(event)">Dictate</a>
			</div>

			<div id="results">
			  <span id="final_span" class="final"></span>
			  <span id="interim_span" class="interim"></span>
			</div>

			<script type="text/javascript">
			var final_transcript = '';
			var recognizing = false;

			if ('webkitSpeechRecognition' in window) {

			  var recognition = new webkitSpeechRecognition();

			  recognition.continuous = true;
			  recognition.interimResults = true;

			  recognition.onstart = function() {
				recognizing = true;
			  };

			  recognition.onerror = function(event) {
				console.log(event.error);
			  };

			  recognition.onend = function() {
				recognizing = false;
			  };

			  recognition.onresult = function(event) {
				var interim_transcript = '';
				for (var i = event.resultIndex; i < event.results.length; ++i) {
				  if (event.results[i].isFinal) {
					final_transcript += event.results[i][0].transcript;
				  } else {
					interim_transcript += event.results[i][0].transcript;
				  }
				}
				final_transcript = capitalize(final_transcript);
				final_span.innerHTML = linebreak(final_transcript);
				interim_span.innerHTML = linebreak(interim_transcript);
				
			  };
			}

			var two_line = /\n\n/g;
			var one_line = /\n/g;
			function linebreak(s) {
			  return s.replace(two_line, '<p></p>').replace(one_line, '<br>');
			}

			function capitalize(s) {
			  return s.replace(s.substr(0,1), function(m) { return m.toUpperCase(); });
			}

			function startDictation(event) {
			  if (recognizing) {
				recognition.stop();
				return;
			  }
			  final_transcript = '';
			  recognition.lang = 'en-US';
			  recognition.start();
			  final_span.innerHTML = '';
			  interim_span.innerHTML = '';
			}
			</script>
	</body>
</html