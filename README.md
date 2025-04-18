# Fakehttpstatus

## Description

Only for study, not commercial stuff. Fully open source.

A simple tiny solution for collecting and displaying http status.

Based on python, designed for running on riscv machines. @~@


## Progress

Currently in the very beginning stage... I suppose...

---- Apr 15 2025

Codes mostly done rn, probably require some tests.

And now working on building packages for riscv.

---- Apr 16 2025

Already added riscv support: check directory rpm

Next stage we plan to run it on a riscv board(display messages that user put in the board, maybe...

---- Apr 17 2025

Problem associated with python package <requests> identified. 

Only occurs on riscv version. Might be resolved really quick!

Stay tuned...

(several hrs later) Fixed rn! No need to import!

---- Apr 18 2025

## Member
* [ChestNutICE](https://github.com/ChestNutICE): Coding
* [Mizi](https://github.com/Mizi-mizi): Coding
* [sychen-o](https://github.com/sychen-o): Testing

## Issue

If you meet any problem with running this program,

first you can try to `chmod +x /usr/bin/fakehttp`,

then try to run it again.

If it is related to [SSL: CERTIFICATE_VERIFY_FAILED], try to adjust the date on your machine

Any further questions, please email <sudoavocado@gmail.com>
