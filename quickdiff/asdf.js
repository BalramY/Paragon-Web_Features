
    {
        label: "LABELXXXXXXXXXXXXXX",
        value: sheetEq?.PROPERTY_VALUEXXXXXXXXXXXX,
        type: "text",
        length: null,
        defaultValueForPicker: "",
        picker: null,
        pickerOptions: null,
        placeholder: null,
        custom: false,
        visible:  true, // Conditions for visibility of particular property
        customComponent: null,
        moldProperty: true,
        property: "PROPERTY_VALUEXXXXXXXXXXXX",
        unitProperty: null,
        table: "Sheet",
      },
      
    {
        label: "Conductor Size",
        value: sheetEq?.cable_size,
        type: "numeric",
        length: 5,
        defaultValueForPicker: sheetEq?.cable_size_units,
        picker: "select",
        pickerOptions: {
          PAS: "MCM",
          option2: "/0 AWG",
        },
        placeholder: null,
        custom: false,
        visible: eqType?.is_cable, // Conditions for visibility of particular property
        customComponent: null,
        moldProperty: true,
        property: "cable_size",
        unitProperty: "cable_size_units",
        table: "Sheet",
      },