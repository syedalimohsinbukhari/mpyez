bash ./shell_scripts/linting.sh
echo "Done Linting"
echo ""
bash ./do_tests.sh
echo "Done Coverage"
echo ""
bash ./shell_scripts/build_wheel.sh
echo "Built the wheel"
echo ""