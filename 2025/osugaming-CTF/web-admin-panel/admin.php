<?php
  session_start();
  if (!isset($_SESSION["logged_in"])) {
    header("Location: index.php");
    exit();
  }

  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_FILES["file"])) {
      $file = $_FILES["file"];
      $filename = $file["name"];
      $contents = file_get_contents($file["tmp_name"]);

      if (stripos($filename, ".php") !== false) {
        echo "<h1>file is not allowed</h1>";
      }
      else if (stripos($contents, "<?php") !== false) {
        echo "<h1>file has unsafe contents</h1>";
      }
      else {
        move_uploaded_file($file["tmp_name"], "./uploads/" . $filename);
        header("Location: /uploads/" . $filename);
      }
      die();
    }
  }
?>
<!DOCTYPE html>
<html prefix="og: http://ogp.me/ns#" lang="en">
  <head>
    <meta name="theme-color" content="#615c70">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- looking at this site is not part of the challenge -->
    <link rel="stylesheet" media="all" href="https://osu-assets.str.lc/assets/css/app.1165affa.css">
    <title>osu!</title>
    <style>
      body {
        --base-hue-default: 255;
        --base-hue-override: 255;
      }
      @media (max-width: 900px) {
        .nav2-header {
          position: relative !important;
        }
      }
    </style>
  </head>
  <body class="t-section osu-layout osu-layout--body osu-layout--body-lazer">
    <div class="nav2-header">
      <div class="nav2-header__body">
        <div class="nav2-header__menu-bg js-nav2--menu-bg" data-visibility="hidden"></div>
        <div class="nav2-header__triangles"></div>
        <div class="nav2-header__transition-overlay"></div>
        <div class="osu-page">
          <div class="nav2 js-nav-button">
            <div class="nav2__colgroup nav2__colgroup--menu js-nav-button--container">
              <div class="nav2__col nav2__col--logo">
                <a href="/" class="nav2__logo-link">
                  <div class="nav2__logo nav2__logo--bg"></div>
                  <div class="nav2__logo"></div>
                </a>
              </div>
              <div class="nav2__col nav2__col--menu">
                <a class="nav2__menu-link-main js-menu" href="/">
                  <span class="u-relative"> home <span class="nav2__menu-link-bar u-section--bg-normal"></span></span>
                </a>
                <a class="nav2__menu-link-main js-menu" href="/admin.php">
                  <span class="u-relative"> admin <span class="nav2__menu-link-bar u-section--bg-normal"></span></span>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="osu-layout__section osu-layout__section--full">
      <div class="header-v4">
        <div class="header-v4__container header-v4__container--main">
          <div class="header-v4__bg-container">
            <div class="header-v4__bg "></div>
          </div>
          <div class="header-v4__content">
            <div class="header-v4__row header-v4__row--title">
              <div class="header-v4__icon"></div>
              <div class="header-v4__title"> admin panel </div>
            </div>
          </div>
        </div>
      </div>
      <div class="osu-page osu-page--generic-compact">
        <div class="user-profile-pages user-profile-pages--no-tabs">
          <div class="page-extra">
            <h2 class="title title--page-extra"> system stats </h2>
            <?php
              $uptime = file_get_contents("/proc/uptime");
              $uptime = explode(" ", $uptime);
              $uptime = $uptime[0];
              $uptime = floor($uptime / 60);
              echo "<h6>uptime: $uptime minutes</h6>";
            ?>
          </div>
          <div class="page-extra">
            <h2 class="title title--page-extra"> file upload </h2>
            <form method="POST" action="admin.php" enctype="multipart/form-data">
              <input type="file" name="file">
              <br />
              <input type="submit" value="upload" class="btn-osu-big btn-osu-big--account-edit">
            </form>
          </div>
        </div>
      </div>
    </div>
    <footer class="no-print footer">
      <div class="footer__row">
        <a class="footer__link" href="https://osugaming.sekai.team"> CTF </a>
      </div>
      <div class="footer__row">
        this site is not officially affiliated with osu!
      </div>
    </footer>
  </body>
</html>