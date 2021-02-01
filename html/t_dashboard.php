<?php
$arrHostapdConf = parse_ini_file(RASPI_CONFIG.'/hostapd.ini');

$client_interface = $_SESSION['wifi_client_interface'];

$ap_iface = $_SESSION['ap_interface'];
$MACPattern = '"([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}"';
if ($arrHostapdConf['BridgedEnable'] == 1) {
    $moreLink = "index.php?page=hostapd_conf";
    exec('iw dev '.$ap_iface.' station dump | grep -oE '.$MACPattern, $clients);
} else {
    $moreLink = "index.php?page=dhcpd_conf";
    exec('cat '.RASPI_DNSMASQ_LEASES.'| grep -E $(iw dev '.$ap_iface.' station dump | grep -oE '.$MACPattern.' | paste -sd "|")', $clients);
}
$ifaceStatus = $wlan0up ? "up" : "down";
?>
<div class="row">
  <div class="col-lg-12">
    <div class="card">
      <div class="card-header">
        <div class="row">
	   <div class="col">
	     <i class="fas fa-tachometer-alt fa-fw mr-2"></i><?php echo _("Dashboard"); ?>
	   </div>
	   <div class="col">
	     <button class="btn btn-light btn-icon-split btn-sm service-status float-right">
		<span class="icon"><i class="fas fa-circle service-status-<?php echo $ifaceStatus ?>"></i></span>
		<span class="text service-status"><?php echo strtolower($ap_iface) .' '. _($ifaceStatus) ?></span>
	      </button>
	   </div>
        </div><!-- /.row -->
      </div><!-- /.card-header -->

      <div class="card-body">
	<h4><?php echo _("Configuration") ;?></h4>
	<div class="row">
	  <div class="form-group col-xs-3 col-sm-3">
            <?php $conv = $statusRobot ? 'ON' : 'OFF';?>
            <label for="on_off"><?php echo _("Current Status: $conv"); ?></label>
	    <form action="?page=wlan0_info" method="POST">
	      <?php echo CSRFTokenFieldTag() ?>
	      <?php if (!RASPI_MONITOR_ENABLED) : ?>
		<?php if (!$statusRobot) : ?>
		  <input type="submit" class="btn btn-danger" value="<?php echo _("Turn On")?>" name="on" />
		<?php else : ?>
		  <input type="submit" class="btn btn-success" value="<?php echo _("Turn Off")?>"  name="off" />
		<?php endif ?>
	      <?php endif ?>
	    </form>
	  </div>
	  <div class="col-xs-3 col-sm-3">
            <?php $conv = $auto ? 'AUTO' : 'MANUAL';?>
            <label for="man_auto"><?php echo _("Current Mode: $conv"); ?></label>
	    <form action="?page=wlan0_info" method="POST">
	      <?php echo CSRFTokenFieldTag() ?>
	      <?php if (!RASPI_MONITOR_ENABLED) : ?>
		<?php if (!$auto) : ?>
		  <input type="submit" class="btn btn-danger" value="<?php echo _("Set Auto Mode")?>" name="auto" />
		<?php else : ?>
		  <input type="submit" class="btn btn-success" value="<?php echo _("Set Manual Mode")?>"  name="man" />
		<?php endif ?>
	      <?php endif ?>
	    </form>
	  </div>
	</div>
	
	<form role="form" action="?page=wlan0_info" method="POST">
            <?php echo CSRFTokenFieldTag() ?>
	<div class="row">
	  <div class="form-group col-xs-3 col-sm-3">
            <label for="x0"><?php echo _("Starting X coordinate"); ?></label>
              <input type="text" class="form-control" name="x0" value="<?php echo $coord['x0']; ?>"/>
	  </div>
	  <div class="col-xs-3 col-sm-3">
            <label for="y0"><?php echo _("Starting Y coordinate"); ?></label>
              <input type="text" class="form-control" name="y0" value="<?php echo $coord['y0']; ?>"/>
	  </div>
        </div>

	<div class="row">
	  <div class="form-group col-xs-3 col-sm-3">
            <label for="x1"><?php echo _("Ending X coordinate"); ?></label>
              <input type="text" class="form-control" name="x1" value="<?php echo $coord['x1']; ?>"/>
	  </div>
	  <div class="col-xs-3 col-sm-3">
            <label for="y1"><?php echo _("Ending Y coordinate"); ?></label>
              <input type="text" class="form-control" name="y1" value="<?php echo $coord['y1']; ?>"/>
	  </div>
        </div>
	<input type="submit" class="btn btn-outline btn-warning" name="UpdatePoint" value="<?php echo _("Save settings"); ?>" />
        <a href="?page=<?php echo $_GET['page'] ?>" class="btn btn-outline btn-primary"><i class="fas fa-sync-alt"></i> <?php echo _("Refresh") ?></a>
        </form>

      </div>
	  

      <div class="col-lg-6">
        <div class="card mb-3">
          <div class="card-body">
          <h4><?php echo _("Manual Control"); ?></h4>
	    <div class="row">
	      <div class="col-sm-4">
              </div>
	      <div class="col-sm-4 text-center">
                <label for="f"></label>
	        <form action="?page=wlan0_info" method="POST">
	          <?php echo CSRFTokenFieldTag() ?>
		  <input type="submit" class="btn btn-success" value="<?php echo _("Forward")?>" name="f" />
	        </form>
	      </div>
            </div>
	    <div class="row">
	      <div class="col-sm-4 text-center">
                <label for="l"></label>
	        <form action="?page=wlan0_info" method="POST">
	          <?php echo CSRFTokenFieldTag() ?>
		  <input type="submit" class="btn btn-success" value="<?php echo _("Turn Left")?>" name="l" />
	        </form>
	      </div>
	      <div class="col-sm-4 text-center">
                <label for="s"></label>
	        <form action="?page=wlan0_info" method="POST">
	          <?php echo CSRFTokenFieldTag() ?>
		  <input type="submit" class="btn btn-danger" value="<?php echo _("Stop")?>" name="s" />
	        </form>
	      </div>
	      <div class="col-sm-4 text-center">
                <label for="r"></label>
	        <form action="?page=wlan0_info" method="POST">
	          <?php echo CSRFTokenFieldTag() ?>
		  <input type="submit" class="btn btn-success" value="<?php echo _("Turn Right")?>" name="r" />
	        </form>
	      </div>
	    </div>
	    <div class="row">
	      <div class="col-sm-4">
              </div>
	      <div class="col-sm-4 text-center">
                <label for="b"></label>
	        <form action="?page=wlan0_info" method="POST">
	          <?php echo CSRFTokenFieldTag() ?>
		  <input type="submit" class="btn btn-success" value="<?php echo _("Backwards")?>" name="b" />
	        </form>
	      </div>
            </div>
          </div><!-- /.card-body -->
        </div><!-- /.card-->
      </div>


          <div class="col-sm-6 align-items-stretch">
            <div class="card h-100">
              <div class="card-body wireless">
                <h4><?php echo _("Wireless Client"); ?></h4>
                <div class="row justify-content-md-center">
                <div class="col-md">
                <div class="info-item"><?php echo _("Connected To"); ?></div><div><?php echo htmlspecialchars($connectedSSID, ENT_QUOTES); ?></div>
                <div class="info-item"><?php echo _("Interface"); ?></div><div><?php echo htmlspecialchars($_SESSION['wifi_client_interface']); ?></div>
                <div class="info-item"><?php echo _("AP Mac Address"); ?></div><div><?php echo htmlspecialchars($connectedBSSID, ENT_QUOTES); ?></div>
                <div class="info-item"><?php echo _("Bitrate"); ?></div><div><?php echo htmlspecialchars($bitrate, ENT_QUOTES); ?></div>
                <div class="info-item"><?php echo _("Signal Level"); ?></div><div><?php echo htmlspecialchars($signalLevel, ENT_QUOTES); ?></div>
                <div class="info-item"><?php echo _("Transmit Power"); ?></div><div><?php echo htmlspecialchars($txPower, ENT_QUOTES); ?></div>
                <div class="info-item"><?php echo _("Frequency"); ?></div><div><?php echo htmlspecialchars($frequency, ENT_QUOTES); ?></div>
              </div>
              <div class="col-md mt-2 d-flex justify-content-center">
                <script>var linkQ = <?php echo json_encode($strLinkQuality); ?>;</script>
                <div class="chart-container">
                  <canvas id="divChartLinkQ"></canvas>
                </div>
                </div><!--row-->
              </div>
             </div><!-- /.card-body -->
            </div><!-- /.card -->
          </div><!-- /.col-md-6 -->
          <div class="col-sm-6">
            <div class="card h-100 mb-3">
              <div class="card-body">
                <h4><?php echo _("Connected Devices"); ?></h4>
                <div class="table-responsive">
                  <table class="table table-hover">
                    <thead>
                      <tr>
                        <?php if ($arrHostapdConf['BridgedEnable'] == 1) : ?>
                          <th><?php echo _("MAC Address"); ?></th>
                        <?php else : ?>
                          <th><?php echo _("Host name"); ?></th>
                          <th><?php echo _("IP Address"); ?></th>
                          <th><?php echo _("MAC Address"); ?></th>
                        <?php endif; ?>
                      </tr>
                    </thead>
                    <tbody>
                        <?php if ($arrHostapdConf['BridgedEnable'] == 1) : ?>
                          <tr>
                            <td><small class="text-muted"><?php echo _("Bridged AP mode is enabled. For Hostname and IP, see your router's admin page.");?></small></td>
                          </tr>
                        <?php endif; ?>
                        <?php foreach (array_slice($clients,0, 2) as $client) : ?>
                        <tr>
                          <?php if ($arrHostapdConf['BridgedEnable'] == 1): ?>
                            <td><?php echo htmlspecialchars($client, ENT_QUOTES) ?></td>
                          <?php else : ?>
                            <?php $props = explode(' ', $client) ?>
                            <td><?php echo htmlspecialchars($props[3], ENT_QUOTES) ?></td>
                            <td><?php echo htmlspecialchars($props[2], ENT_QUOTES) ?></td>
                            <td><?php echo htmlspecialchars($props[1], ENT_QUOTES) ?></td>
                          <?php endif; ?>
                        </tr>
                        <?php endforeach ?>
                    </tbody>
                  </table>
                  <?php if (sizeof($clients) >2) : ?>
                      <div class="col-lg-12 float-right">
                        <a class="btn btn-outline-info" role="button" href="<?php echo $moreLink ?>"><?php echo _("More");?>  <i class="fas fa-chevron-right"></i></a>
                      </div>
                  <?php elseif (sizeof($clients) ==0) : ?>
                      <div class="col-lg-12 mt-3"><?php echo _("No connected devices");?></div>
                  <?php endif; ?>
                </div><!-- /.table-responsive -->
              </div><!-- /.card-body -->
            </div><!-- /.card -->
          </div><!-- /.col-md-6 -->
        </div><!-- /.row -->

        <div class="col-lg-12 mt-3">
          <div class="row">
            <form action="?page=wlan0_info" method="POST">
                <?php echo CSRFTokenFieldTag() ?>
                <?php if (!RASPI_MONITOR_ENABLED) : ?>
                    <?php if (!$wlan0up) : ?>
                    <input type="submit" class="btn btn-success" value="<?php echo _("Start").' '.$client_interface ?>" name="ifup_wlan0" />
                    <?php else : ?>
                    <input type="submit" class="btn btn-warning" value="<?php echo _("Stop").' '.$client_interface ?>"  name="ifdown_wlan0" />
                    <?php endif ?>
                <?php endif ?>
              <a href="?page=<?php echo $_GET['page'] ?>" class="btn btn-outline btn-primary"><i class="fas fa-sync-alt"></i> <?php echo _("Refresh") ?></a>
            </form>
          </div>
        </div>

      </div><!-- /.card-body -->
      <div class="card-footer"><?php echo _("Information provided by ip and iw and from system"); ?></div>
    </div><!-- /.card -->
  </div><!-- /.col-lg-12 -->
</div><!-- /.row -->
<script type="text/javascript"<?php //echo ' nonce="'.$csp_page_nonce.'"'; ?>>
// js translations:
var t = new Array();
t['send'] = '<?php echo addslashes(_('Send')); ?>';
t['receive'] = '<?php echo addslashes(_('Receive')); ?>';
</script>
