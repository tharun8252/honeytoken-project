# ✅ Install necessary certificates for secure communication with Splunk
!ls -lh splunk_cert.pem
!cat splunk_cert.pem >> /etc/ssl/certs/ca-certificates.crt
!sudo cp splunk_cert.pem /usr/local/share/ca-certificates/splunk_cert.crt
!sudo update-ca-certificates --fresh
!cat splunk_cert.pem | sudo tee -a /etc/ssl/certs/ca-certificates.crt > /dev/null
!openssl s_client -showcerts -connect prd-p-538gt.splunkcloud.com:8088 </dev/null 2>/dev/null | sed -n '/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p' > splunk_ca.pem
!sudo cp splunk_ca.pem /usr/local/share/ca-certificates/splunk_ca.crt
!sudo update-ca-certificates --fresh
!openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt splunk_cert.pem
