<?php
$records_per_page = 10;
$pageNumber = 1;
$pagesCount = 4;
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="assets/img/favicon.ico">

    <title>Medical Robots Research Group</title>

    <!-- Bootstrap core CSS -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="assets/css/custom.css" rel="stylesheet">
    <style>
    </style>
    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>
        <!-- Fixed navbar -->
    <div class="navbar navbar-default navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Medical Robots</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li><a href="index.php">Home</a></li>
            <li class="active"><a href="researchthemes.php">Research</a></li>
            <li><a href="equipements.php">Equipements</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">About <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="members.php">People</a></li>
                <li><a href="objectives.php">Objectives</a></li>
                <li><a href="achievements.php">Achievements</a></li>
              </ul>
            </li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>
    <!-- container -->
    <div class="container">
      <?php for($i=0; $i < $records_per_page; $i++) {?>
        <div class="row item">
          <div class="col-md-2">
            <a href="researchtheme.php"><img class="small" src="assets/img/research-img.jpg"/></a>
          </div>
          <div class="col-md-9">
            <h3><a href="researchtheme.php">Research Topic Title</a></h3>
            <p>
              Description for research topic. Description for research topic. Description for research topic. 
              Description for research topic. Description for research topic. Description for research topic. 
              Description for research topic.
            </p>
            <p>Supervised By: <a href="member.php">Dr. Islam Shoukry</a></p>
          </div>
        </div>
        <hr class="featurette-divider">
      <?php }?>
      <div class="row">
      <div class="col-md-4"></div>
      <div class="pagination col-md-4">
        <ul class="pagination">
          <li class="disabled"><a href="researchthemes.php">&laquo;</a></li>
          <?php
            for($i = 1; $i <= $pagesCount; $i++)
              echo '<li class="'.($pageNumber==$i?'active':'').'"><a href="researchthemes.php">'.$i.'</a></li>';
            ?>
          <li class="<?php echo $pageNumber==$pagesCount||$pagesCount==0?'disabled':'';?>"><a href="researchthemes.php">&raquo;</a></li>
        </ul>
      </div>
      <div class="col-md-4"></div>
    </div>
    </div> <!-- /container -->
    
    <!-- Site footer -->
    <div id="footer">
      <div class="container">
        <p class="text-muted">Place sticky footer content here.</p>
      </div>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>
  </body>
</html>
