CCTOOLS_HOME = ../../..

include ${CCTOOLS_HOME}/Makefile.config

ccflags=${CCTOOLS_PYTHON_CCFLAGS} -I${CCTOOLS_HOME}/dttools/src
ldflags=${CCTOOLS_PYTHON_LDFLAGS} ${CCTOOLS_HOME}/dttools/src/libdttools.a

# Python always uses 'so' for its modules (even on Darwin)
CCTOOLS_DYNAMIC_SUFFIX=so

all: work_queue.py _work_queue.${CCTOOLS_DYNAMIC_SUFFIX}

work_queue_wrap.c work_queue.py: ../work_queue.i work_queue.binding.py
	@echo "SWIG work_queue.i (python)"
	@${CCTOOLS_SWIG} -python -I${CCTOOLS_HOME}/dttools/src -o work_queue_wrap.c ../work_queue.i
	@cat work_queue.binding.py >> work_queue.py

work_queue_wrap.o: work_queue_wrap.c
	${CCTOOLS_CC} -fPIC -c $< -o $@ ${ccflags}

# The odd symlink in the following rule is necessary to overcome a problem
# in the framework search path emitted by the Python configuration on macOS.

_work_queue.${CCTOOLS_DYNAMIC_SUFFIX}: work_queue_wrap.o
	 @ln -sf /Library/Frameworks/EPD64.framework EPD64.framework
	echo ${CCTOOLS_LD} ${CCTOOLS_DYNAMIC_FLAG} $< -o $@ ${CCTOOLS_INTERNAL_LDFLAGS} ${ldflags}
	echo ${ldflags}
	${CCTOOLS_LD} ${CCTOOLS_DYNAMIC_FLAG} $< -o $@ ${CCTOOLS_INTERNAL_LDFLAGS} ${ldflags}
	 @rm EPD64.framework


test: all
	@echo running work queue python binding tests
	@${CCTOOLS_HOME}/dttools/src/test_runner.sh TR_*.sh

clean:
	rm -fr Python.framework _work_queue.${CCTOOLS_DYNAMIC_SUFFIX} work_queue.py work_queue_wrap.* *.pyc

install: all
	mkdir -p ${CCTOOLS_INSTALL_DIR}/lib/python${CCTOOLS_PYTHON_VERSION}/site-packages
	install _work_queue.${CCTOOLS_DYNAMIC_SUFFIX} ${CCTOOLS_INSTALL_DIR}/lib/python${CCTOOLS_PYTHON_VERSION}/site-packages
	install  work_queue.py ${CCTOOLS_INSTALL_DIR}/lib/python${CCTOOLS_PYTHON_VERSION}/site-packages
