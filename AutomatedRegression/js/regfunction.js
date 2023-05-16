class RegFunction
{
    /**
     * Parametrized Constructor for Reg function
     * @param {string} R2 R-squared
     * @param {string} L upper limit
     * @param {string} C  added constant
     * @param {string} n  growth rate
     * @param {string} SP  setpoint concentration
     * @param {string} comp Sensed species
     */
    constructor(R2, L, C, n, SP, comp, y)
    {
        this.R2 = R2
        this.L = L;
        this.C = C;
        this.n = n;
        this.SP = SP;
        this.comp = comp;
       
        this.y = y; 
    }

   getR2()
   {
       return this.R2; 
   }

   getL()
   {
       return this.L;
   } 
   getC()
   {
       return this.C;
   }
   getN()
   {
       return this.n;
    
   }

   getSP()
   {
       return this.SP;
   }

   getComp()
   {
       return this.comp; 
   }

   getJSON()
   {
       return JSON.stringify(this);
   }

   toString()
   {
       var array = [this.comp, this.y, this.L, this.n, this.SP, this.C, this.R2];
       return array.join(); 
   }
}