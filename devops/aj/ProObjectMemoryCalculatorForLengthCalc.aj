package com.tmax.proobject.test.runtime.servicegroup.main.service.memorycalc;

import com.tmax.proobject.engine.calculator.MemoryCalculator;
import java.util.List;
import java.util.Map;
import java.util.Set;

public aspect ProObjectMemoryCalculatorForLengthCalc {

    /**
     * Map Collection
     */
    pointcut callMapNCollection(): !within(com.tmax.proobject.engine.*) && (within(com.tmax.proobject.model.service.ServiceObject+) || within(com.tmax.proobject.model.business.BusinessObject+)) &&(call(* add*(..)) || call(* put*(..)));

    before() : callMapNCollection() {
        
        int size = 0;
        
        Object object = thisJoinPoint.getTarget();
        if(object instanceof List) {
            List thisList = (List) object;
            size = thisList.size();
        }
        else if(object instanceof Set) {
            Set thisSet = (Set) object;
            size = thisSet.size();
        }
        else if(object instanceof Map) {
            Map thisMap = (Map) object;
            size = thisMap.size();
        }
        
        MemoryCalculator.calculateMapNCollection(thisJoinPoint , size);
    }

}
