from invoke import Collection, Program
import qtemplate

program = Program(namespace=Collection.from_module(qtemplate.qtemplate), version='0.0.1', name="qtemplate (qt)")
