  
describe("Contact Page Testing", function() {

  /*
    I needed to take the functions out of the contacts module to test, so it isn't a 
    verbatim version of the code being tested
  */


  describe("Checking format of date generated as current date", function() { 
      //date object for tests to make sure todays date is used
      var testDate = new Date();
      it("should return date obj for current day in required format", function() {
        //toEqual is needed as comparing Objects
        expect(actualDate()).toEqual({day: testDate.getDate(), month: testDate.getMonth()+1, year: testDate.getFullYear()});
      });
    });    



  describe("Validating Year", function() {
    it("should return 'true' if the recieved year (1st arg) is greater than the current year", function() {
      expect(isYearInFuture(2018, 2017)).toBe(true);
    });

    it("should return 'undefined' if the recieved year (1st arg) is less than the current year", function() {
      expect(isYearInFuture(2017, 2018)).toBeUndefined();
    });

    it("should return 'undefined' if the recieved year (1st arg) is the same as the current year", function() {
      expect(isYearInFuture(2017, 2017)).toBeUndefined();
    });

  });


  describe("Validating Month", function() {
    it("should return 'true' if the recieved month (1st arg) is greater than the current month", function() {
      expect(isYearInFuture(05, 01)).toBe(true);
    });

    it("should return 'undefined' if the recieved month (1st arg) is less than the current month", function() {
      expect(isYearInFuture(01, 05)).toBeUndefined();
    });

    it("should return 'undefined' if the recieved month (1st arg) is the same as the current month", function() {
      expect(isYearInFuture(01, 01)).toBeUndefined();
    });

    it("should return 'true' if the recieved month is greater than 12", function() {
      expect(isMonthOverTwelve(13)).toBe(true);
    });

    it("should return 'undefined' if the recieved month is 12", function() {
      expect(isMonthOverTwelve(12)).toBeUndefined();
    });

    it("should return 'undefined' if the recieved month is less than 12", function() {
      expect(isMonthOverTwelve(10)).toBeUndefined();
    });
  });



  describe("Validating Day", function() {
      var isMonthValid;  

    it("should return 'true' if the recieved day is greater than 31", function() {
      expect(isDayOverThirtyOne(40)).toBe(true);
    });
    it("should return 'undefined' if the recieved day is 31", function() {
      expect(isDayOverThirtyOne(31)).toBeUndefined();
    });
    it("should return 'undefined' if the recieved day is less than 31", function() {
      expect(isDayOverThirtyOne(20)).toBeUndefined();
    });


  });


});
