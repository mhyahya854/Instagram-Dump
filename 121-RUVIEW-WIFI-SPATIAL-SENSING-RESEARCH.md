# 121 — RuView: Wi-Fi Spatial Sensing and Claim Validation

**Original source:** screenshot #1 of fifteenth Instagram batch, exact visible text `Link : https://github.com/ruvnet/ruview`. The screenshot does not demonstrate any hardware, firmware or result.

**Verified repo:** https://github.com/ruvnet/RuView . This project describes experimental Wi-Fi channel-state-information (CSI) sensing for presence/activity and room/spatial estimation with ESP32 or compatible hardware, complementary mmWave radar, and integrations. Associated **MetaHarness** supports guided inspection/device work, permissioned MCP interfaces, read-only default agent runs and evidence-based verification. It is NOT a simple webcam or software-only substitute for physical RF sensing hardware.

## Architecture and ideas captured

1. Acquire appropriate RF signal data (CSI requires supported chipset/firmware), timestamps, calibration, and legal/environmental permission.
2. Build preprocessing/filtering, temporal windowing, baseline room measurements and drift detection.
3. Infer *probabilistic* events with explicit confidence/quality metadata: room activity, movement, possible rest states, etc.; do not promise identification or medical-grade vitals from ordinary routers.
4. Separate simulated contract tests, demonstrations and **real hardware validation**. The README itself labels many numeric accuracy/pose/vital claims experimental or unvalidated; avoid presenting synthetic results as field performance.
5. Offer a privacy-conscious local deployment and data minimization by default, with opt-in room sensing and review of who could be monitored.
6. Verify hardware variants, flashing risk, network segmentation, firmware supply chain, MQTT/Matter/Home Assistant permissions, model accuracy and human-consent policy.

## Why the repo matters

Useful architecture reference for ambient sensing, occupancy-based automation and edge-device orchestration, not a guaranteed human detector through any wall or a biometric diagnostic device. The project is under active change; pin releases and examine supported devices. No hardware access, firmware flashing, wireless scanning or tool installation conducted here.

**Source distinction:** typed repo link is directly grounded in image; capabilities come from README and docs; technical caution is independent analysis.
