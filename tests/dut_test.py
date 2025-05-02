import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def dut_test(dut):
    dut.inp.value = 1         
    await Timer(10, units="ns")
    assert dut.out.value == 1 
initial begin
    $dumpfile("tests/dut.vcd");    
    $dumpvars(0, dut);    
end
