Application:
It’s a full featured e-commerce website simulator, Here you can test anything from a simple login page to product selection and add/edit your shopping cart. It covers the complete online shopping workflow. You can write Selenium scripts to fill address, shipping details, and proceed to simulate payment.
AUT: http://automationpractice.com/index.php

Framework & Tools:
It is designed using pytest framework with selenium, using python as core coding language. This has log generation, report generation with html report plugins.
Frameweork built on Page Object Model design pattern and Page chaining Model design.

Execution:
2 ways to run the tests:
1. Using Terminal:
    py.test -v -s --browser_name=<browserName> ----> browserName can be Safari/Chrome/Edge/Brave/Firefox
    py.test --html=report.html ----> Generates html.report
    To store scripts in report location: py.test --html=./webPytestEcommerceProj/reports/report.html
2. Using PyCharm IDE, configuring pytest.
